import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *


class app_UI_form(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("PyQT5 Test!")
        self.setGeometry(800, 400, 500, 400)

        UI_label1 = QLabel("입력", self)
        UI_label2 = QLabel("출력", self)

        UI_label1.move(20, 20)
        UI_label2.move(20, 60)

        self.UI_lineEdit = QLineEdit("", self)  # default value
        self.UI_plainEdit = QtWidgets.QPlainTextEdit(self)  # 다기능 글자 편집기
        self.UI_plainEdit.setReadOnly(True)

        self.UI_lineEdit.move(90, 20)
        self.UI_plainEdit.setGeometry(QtCore.QRect(20, 90, 361, 231))

        self.UI_lineEdit.textChanged.connect(self.UI_lineEdit_changed)  # textChanged()은 시그널, connec는 연결, UI_lineEdit_changed()는 slot
        self.UI_lineEdit.returnPressed.connect(self.UI_lineEdit_enter)

        # 상태바
        self.UI_statusBar = QStatusBar(self)
        self.setStatusBar(self.UI_statusBar)

    def UI_lineEdit_changed(self):  # slot
        self.UI_statusBar.showMessage(self.UI_lineEdit.text())

    def UI_lineEdit_enter(self):  # slot
        self.UI_plainEdit.appendPlainText(self.UI_lineEdit.text())  # insert는 줄바꿈 X, append는 O
        self.UI_lineEdit.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = app_UI_form()
    window.show()

    app.exec_()

# QMainWindow : 상태바 등 기본 레이아웃이 있는 Window
# QApplication : Empty Window

# 시그널 : 이벤트 발생
# 슬롯 : 이벤트 처리