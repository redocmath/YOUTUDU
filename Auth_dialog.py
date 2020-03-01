# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Auth_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3
import time


class Auth_Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.user_list = []

    def setupUI(self):
        self.setObjectName("Dialog")
        self.resize(362, 350)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(362, 350))
        self.setMaximumSize(QtCore.QSize(362, 350))
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(70, 10, 231, 71))
        font = QtGui.QFont()
        font.setFamily("BM Hanna 11yrs Old")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 321, 20))
        font = QtGui.QFont()
        font.setFamily("BM Hanna 11yrs Old")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(7, 120, 351, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(40, 180, 60, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(20, 220, 71, 16))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.line_2 = QtWidgets.QFrame(self)
        self.line_2.setGeometry(QtCore.QRect(90, 180, 20, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self)
        self.line_3.setGeometry(QtCore.QRect(90, 220, 20, 21))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.id = QtWidgets.QLineEdit(self)
        self.id.setGeometry(QtCore.QRect(110, 180, 211, 21))
        self.id.setObjectName("id")
        self.pw = QtWidgets.QLineEdit(self)
        self.pw.setGeometry(QtCore.QRect(110, 220, 211, 21))
        self.pw.setObjectName("pw")
        self.pw.setEchoMode(QLineEdit().Password)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(110, 280, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.submitLogin)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Login"))
        self.label.setText(_translate("Dialog", "Log IN"))
        self.label_2.setText(_translate("Dialog", "Log IN is happy, and EveryThing is good!"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">id</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Password</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Let\'s Go!"))

    def submitLogin(self):
        self.user_id = self.id.text()
        self.user_pw = self.pw.text()

        if self.user_id is None or self.user_id == '' or not self.user_id:
            QMessageBox.about(self, "Auth Error", "please input id")
            self.id.setFocus(True)
            return

        if self.user_pw is None or self.user_pw == '' or not self.user_pw:
            QMessageBox.about(self, "Auth Error", "please input pw")
            self.pw.setFocus(True)
            return

        # SQL
        _connect = sqlite3.connect('database/user.db', isolation_level=None)
        SQL = _connect.cursor()
        SQL.execute('CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY, username text, password text)')
        SQL.execute('SELECT * from users')
        self.user_list = SQL.fetchall()

        is_null = False
        is_correct = False
        for user_info in self.user_list:
            if self.user_id == user_info[1]:
                if self.user_pw == user_info[2]:
                    is_correct = True
                    is_null = True
                else:
                    is_correct = False
                    is_null = True
                    break

        exit_ = False
        if is_null:
            if is_correct:
                QMessageBox.about(self, 'Auth Alert', '로그인 성공!')
                exit_ = True
            else:
                QMessageBox.about(self, 'Auth Alert', '패스워드가 틀렸습니다.')
                self.pw.setFocus(True)
        else:
            SQL.execute("INSERT INTO users(id, username, password) VALUES (?, ?, ?)", (len(self.user_list) + 1, self.user_id, self.user_pw))
            QMessageBox.about(self, 'Auth Alert', 'id가 존재하지 않았습니다. 자동 회원가입되었습니다')
            exit_ = True
        if exit_:
            self.user_correct = True
            self.close()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = Auth_Dialog()
    ui.show()
    app.exec_()
