# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MW_zxf.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys



class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.infoTxtlbl = QtWidgets.QLabel(self.centralwidget)
        self.infoTxtlbl.setGeometry(QtCore.QRect(10, 10, 561, 111))
        self.infoTxtlbl.setLineWidth(12)
        self.infoTxtlbl.setText("")
        self.infoTxtlbl.setOpenExternalLinks(False)
        self.infoTxtlbl.setObjectName("infoTxtlbl")
        self.TdoseE = QtWidgets.QLineEdit(self.centralwidget)
        self.TdoseE.setGeometry(QtCore.QRect(90, 170, 61, 24))
        self.TdoseE.setFocusPolicy(QtCore.Qt.TabFocus)
        self.TdoseE.setObjectName("TdoseE")
        self.chBtn = QtWidgets.QPushButton(self.centralwidget)
        self.chBtn.setGeometry(QtCore.QRect(680, 20, 89, 24))
        self.chBtn.setFocusPolicy(QtCore.Qt.TabFocus)
        self.chBtn.setObjectName("chBtn")
        self.rtidTxt = QtWidgets.QLineEdit(self.centralwidget)
        self.rtidTxt.setGeometry(QtCore.QRect(580, 20, 89, 24))
        self.rtidTxt.setObjectName("rtidTxt")
        self.beamNumB = QtWidgets.QLineEdit(self.centralwidget)
        self.beamNumB.setGeometry(QtCore.QRect(10, 170, 61, 24))
        self.beamNumB.setFocusPolicy(QtCore.Qt.TabFocus)
        self.beamNumB.setObjectName("beamNumB")
        self.infoLst = QtWidgets.QTableView(self.centralwidget)
        self.infoLst.setGeometry(QtCore.QRect(10, 200, 781, 341))
        self.infoLst.setFocusPolicy(QtCore.Qt.TabFocus)
        self.infoLst.setObjectName("infoLst")
        self.docmkBtn = QtWidgets.QPushButton(self.centralwidget)
        self.docmkBtn.setGeometry(QtCore.QRect(610, 170, 83, 24))
        self.docmkBtn.setObjectName("docmkBtn")
        self.bookmkBtn = QtWidgets.QPushButton(self.centralwidget)
        self.bookmkBtn.setGeometry(QtCore.QRect(700, 170, 83, 24))
        self.bookmkBtn.setObjectName("bookmkBtn")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(550, 170, 47, 23))
        self.toolButton.setObjectName("toolButton")
        self.startDateE = QtWidgets.QLineEdit(self.centralwidget)
        self.startDateE.setGeometry(QtCore.QRect(170, 170, 61, 24))
        self.startDateE.setObjectName("startDateE")
        self.sectNumE = QtWidgets.QLineEdit(self.centralwidget)
        self.sectNumE.setGeometry(QtCore.QRect(250, 170, 61, 24))
        self.sectNumE.setObjectName("sectNumE")
        self.BeamNumlbl = QtWidgets.QLabel(self.centralwidget)
        self.BeamNumlbl.setGeometry(QtCore.QRect(10, 140, 68, 16))
        self.BeamNumlbl.setObjectName("BeamNumlbl")
        self.Tdoselbl = QtWidgets.QLabel(self.centralwidget)
        self.Tdoselbl.setGeometry(QtCore.QRect(100, 140, 68, 16))
        self.Tdoselbl.setObjectName("Tdoselbl")
        self.startDatelbl = QtWidgets.QLabel(self.centralwidget)
        self.startDatelbl.setGeometry(QtCore.QRect(170, 140, 68, 16))
        self.startDatelbl.setObjectName("startDatelbl")
        self.secNumlbl = QtWidgets.QLabel(self.centralwidget)
        self.secNumlbl.setGeometry(QtCore.QRect(250, 140, 68, 16))
        self.secNumlbl.setObjectName("secNumlbl")
        self.firmStyle = QtWidgets.QComboBox(self.centralwidget)
        self.firmStyle.setGeometry(QtCore.QRect(330, 170, 86, 24))
        self.firmStyle.setCurrentText("")
        self.firmStyle.setObjectName("firmStyle")
        self.stylelbl = QtWidgets.QLabel(self.centralwidget)
        self.stylelbl.setGeometry(QtCore.QRect(330, 140, 68, 16))
        self.stylelbl.setObjectName("stylelbl")
        self.ExdoseE = QtWidgets.QLineEdit(self.centralwidget)
        self.ExdoseE.setGeometry(QtCore.QRect(430, 170, 51, 24))
        self.ExdoseE.setObjectName("ExdoseE")
        self.Exdoselbl = QtWidgets.QLabel(self.centralwidget)
        self.Exdoselbl.setGeometry(QtCore.QRect(430, 140, 68, 16))
        self.Exdoselbl.setObjectName("Exdoselbl")
        self.LdoseE = QtWidgets.QLineEdit(self.centralwidget)
        self.LdoseE.setGeometry(QtCore.QRect(490, 170, 51, 24))
        self.LdoseE.setObjectName("LdoseE")
        self.Ldoselbl = QtWidgets.QLabel(self.centralwidget)
        self.Ldoselbl.setGeometry(QtCore.QRect(500, 140, 68, 16))
        self.Ldoselbl.setObjectName("Ldoselbl")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.firmStyle.setCurrentIndex(3)
        self.firmStyle.addItem("U型面膜+体架")
        self.firmStyle.addItem("S型面膜+体架")
        self.firmStyle.addItem("真空负压袋")
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.chBtn.setText(_translate("MainWindow", "OK"))
        self.docmkBtn.setText(_translate("MainWindow", "DM"))
        self.bookmkBtn.setText(_translate("MainWindow", "BM"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.BeamNumlbl.setText(_translate("MainWindow", "BeaNu"))
        self.Tdoselbl.setText(_translate("MainWindow", "Tdo"))
        self.startDatelbl.setText(_translate("MainWindow", "StD"))
        self.secNumlbl.setText(_translate("MainWindow", "sec"))
        self.stylelbl.setText(_translate("MainWindow", "style"))
        self.Exdoselbl.setText(_translate("MainWindow", "Ed"))
        self.Ldoselbl.setText(_translate("MainWindow", "Ld"))




"""
if __name__ == "__main__":


    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    #MainWindow.setWindowIcon(QIcon('icon.png'))  #增加icon图标
    MainWindow.show()
    sys.exit(app.exec_())
"""