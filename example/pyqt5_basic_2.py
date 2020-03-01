import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class app_UI_form(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("PyQT5 Test!")
        self.setGeometry(800, 400, 500, 300)

        UI_btn = QPushButton("Click me!", self)
        UI_btn1 = QPushButton("Click me!", self)
        UI_btn2 = QPushButton("Click me!", self)
        UI_btnQuit = QPushButton("Quit me!", self)

        UI_btn.move(20, 20)
        UI_btn1.move(20, 60)
        UI_btn2.move(20, 100)
        UI_btnQuit.move(200, 50)

        UI_btn.clicked.connect(self.UI_btn_clicked) # slot connect
        UI_btn1.clicked.connect(self.UI_btn1_clicked)
        UI_btn2.clicked.connect(self.UI_btn2_clicked)
        UI_btnQuit.clicked.connect(QCoreApplication.instance().quit)


    def UI_btn_clicked(self):
        QMessageBox.about(self, "message", "btn Clicked")

    def UI_btn1_clicked(self):
        QMessageBox.about(self, "message", "btn1 Clicked")

    def UI_btn2_clicked(self):
        QMessageBox.about(self, "message", "btn2 Clicked")



if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = app_UI_form()
    window.show()

    app.exec_()

# QMainWindow : 상태바 등 기본 레이아웃이 있는 Window
# QApplication : Empty Window

# 시그널 : 이벤트 발생
# 슬롯 : 이벤트 처리