# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'colored_button.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.colorButton = QtWidgets.QPushButton(self.centralwidget)
        self.colorButton.setGeometry(QtCore.QRect(430, 130, 350, 201))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.colorButton.setFont(font)
        self.colorButton.setStyleSheet("background-color: rgb(46, 204, 113); border: none;")
        self.colorButton.setObjectName("colorButton")
        self.okButton = QtWidgets.QPushButton(self.centralwidget)
        self.okButton.setGeometry(QtCore.QRect(670, 20, 107, 30))
        self.okButton.setObjectName("okButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(500, 100, 211, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 530, 81, 18))
        self.label_2.setObjectName("label_2")
        self.messageLabel = QtWidgets.QLabel(self.centralwidget)
        self.messageLabel.setGeometry(QtCore.QRect(110, 530, 671, 20))
        self.messageLabel.setText("")
        self.messageLabel.setObjectName("messageLabel")
        self.hexColor = QtWidgets.QLineEdit(self.centralwidget)
        self.hexColor.setGeometry(QtCore.QRect(22, 20, 641, 30))
        self.hexColor.setObjectName("hexColor")
        self.pasteButton = QtWidgets.QPushButton(self.centralwidget)
        self.pasteButton.setGeometry(QtCore.QRect(555, 60, 107, 30))
        self.pasteButton.setObjectName("pasteButton")
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(670, 60, 107, 30))
        self.resetButton.setObjectName("resetButton")
        self.originalColorButton = QtWidgets.QPushButton(self.centralwidget)
        self.originalColorButton.setGeometry(QtCore.QRect(20, 130, 350, 391))
        self.originalColorButton.setStyleSheet("background-color: rgb(46, 204, 113); border: none;")
        self.originalColorButton.setObjectName("originalColorButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 100, 121, 18))
        self.label_3.setObjectName("label_3")
        self.colorResult = QtWidgets.QTextEdit(self.centralwidget)
        self.colorResult.setGeometry(QtCore.QRect(430, 340, 350, 181))
        self.colorResult.setStyleSheet("background-color: lightgray")
        self.colorResult.setObjectName("colorResult")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.resetButton.clicked.connect(self.hexColor.clear)
        self.resetButton.clicked.connect(self.messageLabel.clear)
        self.resetButton.clicked.connect(self.hexColor.setFocus)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Closest X11 Color"))
        self.colorButton.setText(_translate("MainWindow", "Color"))
        self.okButton.setText(_translate("MainWindow", "OK"))
        self.label.setText(_translate("MainWindow", "Closest X11 color (0..255):"))
        self.label_2.setText(_translate("MainWindow", "Message:"))
        self.hexColor.setPlaceholderText(_translate("MainWindow", "#ABCDEF"))
        self.pasteButton.setText(_translate("MainWindow", "Paste"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))
        self.originalColorButton.setText(_translate("MainWindow", "Color"))
        self.label_3.setText(_translate("MainWindow", "Original color:"))

