import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from pyqt5_basic_ui import Ui_MainWindow

form_class = uic.loadUiType('UI/UI_basic.ui')[0]


class app_UI_form(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = app_UI_form()
    window.show()

    app.exec_()

# QMainWindow : 상태바 등 기본 레이아웃이 있는 Window
# QApplication : Empty Window

# 시그널 : 이벤트 발생
# 슬롯 : 이벤트 처리