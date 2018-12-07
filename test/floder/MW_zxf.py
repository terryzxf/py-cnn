# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MW_zxf.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Mwindow(object):
    def setupUi(self, Mwindow):
        Mwindow.setObjectName("Mwindow")
        Mwindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Mwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.infoLbl = QtWidgets.QLabel(self.centralwidget)
        self.infoLbl.setGeometry(QtCore.QRect(10, 10, 591, 71))
        self.infoLbl.setText("")
        self.infoLbl.setObjectName("infoLbl")
        self.rtidEdt = QtWidgets.QLineEdit(self.centralwidget)
        self.rtidEdt.setGeometry(QtCore.QRect(680, 10, 113, 24))
        self.rtidEdt.setObjectName("rtidEdt")
        self.chkBtn = QtWidgets.QPushButton(self.centralwidget)
        self.chkBtn.setGeometry(QtCore.QRect(690, 60, 80, 24))
        self.chkBtn.setObjectName("chkBtn")
        self.infoTbl = QtWidgets.QTableView(self.centralwidget)
        self.infoTbl.setGeometry(QtCore.QRect(10, 161, 781, 381))
        self.infoTbl.setObjectName("infoTbl")
        self.docBtn = QtWidgets.QPushButton(self.centralwidget)
        self.docBtn.setGeometry(QtCore.QRect(560, 120, 83, 24))
        self.docBtn.setObjectName("docBtn")
        self.recBtn = QtWidgets.QPushButton(self.centralwidget)
        self.recBtn.setGeometry(QtCore.QRect(670, 120, 83, 24))
        self.recBtn.setObjectName("recBtn")
        Mwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Mwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Mwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Mwindow)
        self.statusbar.setObjectName("statusbar")
        Mwindow.setStatusBar(self.statusbar)

        self.retranslateUi(Mwindow)
        self.chkBtn.clicked.connect(Mwindow.chkBtn_Clk)
        self.docBtn.clicked.connect(Mwindow.docBtn_Clk)
        self.recBtn.clicked.connect(Mwindow.recBtn_Clk)
        QtCore.QMetaObject.connectSlotsByName(Mwindow)
        Mwindow.setTabOrder(self.chkBtn, self.rtidEdt)
        Mwindow.setTabOrder(self.rtidEdt, self.infoTbl)
        Mwindow.setTabOrder(self.infoTbl, self.docBtn)
        Mwindow.setTabOrder(self.docBtn, self.recBtn)

    def retranslateUi(self, Mwindow):
        _translate = QtCore.QCoreApplication.translate
        Mwindow.setWindowTitle(_translate("Mwindow", "zxF"))
        self.chkBtn.setText(_translate("Mwindow", "OK"))
        self.docBtn.setText(_translate("Mwindow", "o"))
        self.recBtn.setText(_translate("Mwindow", "k"))

