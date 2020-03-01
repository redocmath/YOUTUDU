import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot, QUrl, QThread
from PyQt5 import uic
from lib.youtudu_v1_layout import UI_MainWindow
from lib.Auth_dialog import Auth_Dialog
from lib.FName_dialog import Ui_FName
from lib.Thread_worker import Thread_worker
import sqlite3
import re
import youtube_dl
import datetime

form_class = uic.loadUiType('UI/youtudu_v1_UI.ui')[0]


class YOUTUDU(QMainWindow, UI_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI(self)
        self.Auth_init_lock()
        self.Signal_init()

        self.user_id = None
        self.is_play = False
        self.youtb = None
        self.youtube_index = None

        # if not thread
        # QSound.play('resource/intro.wav')

        # thread
        self.Thread_init_intro()

    def Thread_init_intro(self):
        self.Thread = Thread_worker()
        self.Intro_thread = QThread()
        self.Thread.moveToThread(self.Intro_thread)

        # signal connect
        self.Thread.start_log.connect(self.Intro_show_Info)

        # thread start signal connect
        self.Intro_thread.started.connect(self.Thread.play_BGM)

        self.Intro_thread.start()

    def Intro_show_Info(self, msg, file):
        self.log.append("program started by : %s" % msg)
        self.log.append("Intro is : %s" % file)

    def Auth_init_lock(self):
        self.url.setText("Login to download file")
        self.url.setEnabled(False)
        self.btn_path.setEnabled(False)
        self.path.setEnabled(False)
        self.stream_comboBox.setEnabled(False)
        self.btn_start.setEnabled(False)
        self.calendarWidget.setEnabled(False)
        self.Statusbar_show('Auth Failed. Please logIn.')

    def Auth_init_active(self):
        self.url.setText("")
        self.url.setEnabled(True)
        self.btn_path.setEnabled(True)
        self.path.setEnabled(True)
        self.stream_comboBox.setEnabled(True)
        self.calendarWidget.setEnabled(True)
        self.Statusbar_show('Auth Success. Welcome, %s!' % self.user_id)

    def Statusbar_show(self, message):
        self.statusbar.showMessage(message)

    @pyqtSlot()
    def Signal_init(self):
        self.LogIN.clicked.connect(self.Auth_check)
        self.btn_stop.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.url.returnPressed.connect(self.URL_load)
        self.webView.loadProgress.connect(self.Progressbar_browser_loading)
        self.btn_path.clicked.connect(self.Path_btn_clicked)
        self.calendarWidget.clicked.connect(self.calenderWidget_clicked)
        self.btn_start.clicked.connect(self.YoutubeDL_download)

    @pyqtSlot()
    def Auth_check(self):
        dialog = Auth_Dialog()
        dialog.exec_()
        self.user_id = dialog.user_id

        if dialog.user_correct: #  dialog.user_correct
            self.Auth_init_active()
            self.LogIN.setText('Auth Finished.')
            self.LogIN.setEnabled(False)
            self.url.setEnabled(True)
            self.Log_append_message("[%s] - login success" % self.user_id)

    def Log_append_message(self, act):
        now = datetime.datetime.now()
        insert_time = now.strftime("%Y-%m-%d %H:%M:%S")

        log_append = '(' + insert_time + ') : ' + act
        self.log.append(log_append)

        _connect = sqlite3.connect('log/log.db', isolation_level=None)
        SQL = _connect.cursor()
        SQL.execute('CREATE TABLE IF NOT EXISTS LOGS(id integer PRIMARY KEY, log text)')
        SQL.execute('SELECT * FROM LOGS')

        log_list = SQL.fetchall()
        SQL.execute('INSERT INTO LOGS(id, log) VALUES (?, ?)', (len(log_list) + 1, log_append))

    @pyqtSlot()
    def URL_load(self):
        self._url = self.url.text().strip()
        comp = re.compile("^https://www.youtube.com/?")

        if self.is_play:
            if self._url == '':
                self.btn_start.setEnabled(False)
                self.is_play = False
                self.Log_append_message('Stop Click')
                self.Statusbar_show('finished playing')
                self.webView.load(QUrl('about:blank'))
            else:
                if comp.match(self._url) is not None:
                    self.Log_append_message("[%s] - play click" % self.user_id)
                    self.webView.load(QUrl(self._url))
                    self.tabWidget.setCurrentIndex(0)
                    self.Statusbar_show(self._url + " is playing")
                    self.url.setText('')
                    self.is_play = True
                    self.btn_start.setEnabled(True)
                else:
                    QMessageBox.about(self, "URL Error", "Not Valid URL.")
                    self.url.clear()
                    self.url.setFocus(True)
            self.download_process.setValue(0)
        else:
            if comp.match(self._url) is not None:
                self.Log_append_message("[%s] - play click" % self.user_id)
                self.webView.load(QUrl(self._url))
                self.tabWidget.setCurrentIndex(0)
                self.Statusbar_show(self._url + " is playing")
                self.url.setText('')
                self.is_play = True
                self.btn_start.setEnabled(True)
                self.YoutubeDL_init()
            else:
                QMessageBox.about(self, "URL Error", "Not Valid URL.")
                self.url.clear()
                self.url.setFocus(True)

    def YoutubeDL_init(self):
        self.youtb = ['audio only - m4a (worst)', '144p - mp4', '240p - mp4', '360p - mp4', '480p - mp4', '720p - mp4', '640p - mp4(with music)', '1080p - mp4 (best)(with music)']
        self.youtube_index = [140, 160, 133, 134, 135, 136, 18, 22]
        self.stream_comboBox.addItems(self.youtb)

    @pyqtSlot(int)
    def Progressbar_browser_loading(self, v):
        self.preview_process.setValue(v)

    @pyqtSlot()
    def Path_btn_clicked(self):
        # file select
        # file_name = QFileDialog.getOpenFileName(self)
        # self.path.setText(file_name[0])

        # path select
        file_path = QFileDialog.getExistingDirectory(self, 'Directory to save')
        self.path.setText(file_path)

    @pyqtSlot()
    def calenderWidget_clicked(self):
        date_now = self.calendarWidget.selectedDate()
        self.log.append("[%s] - selected %s" % (self.user_id, str(date_now.year()) + '-' + str(date_now.month()) + '-' + str(date_now.day())))
        self.Statusbar_show("%s was selected" % (str(date_now.year()) + '-' + str(date_now.month()) + '-' + str(date_now.day())))

    @pyqtSlot()
    def YoutubeDL_download(self):
        if self.path.text() is None or self.path.text() is "":
            QMessageBox.about(self, "Path ERROR", "Not Valid path.")
            self.path.setFocus(True)
            return

        FName = Ui_FName()
        FName.exec_()

        self.fileName = FName.fileName.text()

        download_dir = os.path.join(self.path.text().replace(" ", "_"), self.fileName)

        ydl_opts = {
            'format': self.youtube_index[self.stream_comboBox.currentIndex()],
            'outtmpl': download_dir,
        }

        self.youtubeDL = youtube_dl.YoutubeDL(ydl_opts)
        self.youtubeDL.add_progress_hook(self.showProgressYoutube)
        self.youtubeDL.download([self._url])
        self.Statusbar_show(ydl_opts['outtmpl'] + ' was saved!')
        self.Log_append_message('%s was downloaded.' % ydl_opts['outtmpl'])

    def showProgressYoutube(self, d):
        try:
            self.download_process.setValue(float(d['_percent_str'][2:-1]))
        except KeyError:
            pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    youtudu_main = YOUTUDU()
    youtudu_main.show()
    app.exec_()
