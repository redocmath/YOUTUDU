# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setFileName.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


class Ui_FName(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("FName")
        self.resize(383, 87)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(0, 0))
        self.setMaximumSize(QtCore.QSize(8888888, 16777215))
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 10, 121, 31))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.fileName = QtWidgets.QLineEdit(self)
        self.fileName.setGeometry(QtCore.QRect(150, 10, 221, 31))
        self.fileName.setInputMask("")
        self.fileName.setText("")
        self.fileName.setMaxLength(32767)
        self.fileName.setCursorPosition(0)
        self.fileName.setObjectName("fileName")
        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(130, 10, 20, 30))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(80, 50, 231, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.clicked_btn)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("FName", "Set File Name"))
        self.label.setText(_translate("FName", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">File Name</span></p><p><br/></p></body></html>"))
        self.fileName.setPlaceholderText(_translate("FName", "including Extension"))
        self.pushButton.setText(_translate("FName", "Enter!"))

    def clicked_btn(self):
        self.close()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = Ui_FName()
    ui.show()
    app.exec_()
