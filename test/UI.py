# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sys
import operator  # used for sorting
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QGridLayout, QTableView, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton,QSplitter
#QPushButton #QTextEdit, QGridLayout, QApplication
from PyQt5.QtCore import QAbstractTableModel, Qt, QRect, QCoreApplication
import pandas as pd
import numpy as np


class Ui_Form(QMainWindow):
    def __init__(self, Mwin, dataList, header, *args):
        QMainWindow.__init__(self, *args)
        self.setObjectName("Mwin")
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(70, 70, 1000, 1000)
        self.setWindowTitle("Click on the header to sort table")

        # bind cell click to a method reference
        self.cenwidget = QWidget(Mwin)
        #self.cenwidget.setObjectName("cenwidget")

        self.infoLbl = QLabel(self.cenwidget)
        self.infoLbl.setGeometry(QRect(10, 10, 591, 71))
        self.infoLbl.setText("123")

        self.rtidEdt = QLineEdit(self.cenwidget)
        self.rtidEdt.setGeometry(QRect(680, 10, 113, 24))

        self.chkBtn = QPushButton(self.cenwidget)
        self.chkBtn.setGeometry(QRect(690, 60, 80, 24))

        self.docBtn = QPushButton(self.cenwidget)
        self.docBtn.setGeometry(QRect(560, 120, 83, 24))

        self.recBtn = QPushButton(self.cenwidget)
        self.recBtn.setGeometry(QRect(670, 120, 83, 24))


        #splitter = QSplitter(Qt.Horizontal)

        #Hlayout = QGridLayout(self)
        #Hlayout.setGeometry(QRect(10, 20, 600, 200))
        #Hlayout.alignment('topleft')
        #Hlayout.cellRect(5,4)
        #Hlayout.addWidget(self.docBtn,1,3,2,1)
        #Hlayout.addWidget(self.chkBtn,5,2,1,1)
        #self.setLayout(Hlayout)

        _translate = QCoreApplication.translate
        #self.setWindowTitle(_translate("QWidgt", "zxF"))
        self.chkBtn.setText(_translate("QWidgt", "OK"))
        self.docBtn.setText(_translate("QWidgt", "o"))
        self.recBtn.setText(_translate("QWidgt", "k"))

        #layout = QVBoxLayout(self)
        #layout.setGeometry(QRect(20,300,600,200))
        #layout.addWidget(self.docBtn)
        #self.setLayout(layout)


        #Layout = QVBoxLayout(self)
        #Layout.addWidget(self.infoTbl)
        #self.setLayout(layout)


    def showSelection(self, item):
        cellContent = item.data()
        print(cellContent)  # test
        sf = "  {}  选中 ".format(cellContent)  # sf = "You clicked on {}".format(cellContent)
        # display in title bar for convenience
        self.setWindowTitle(sf)
        """
        # infoTbl
        self.infoTbl = QTableView()
        layout.addWidget(self.infoTbl)
        table_model = MyTableModel(self, dataList, header)
        self.infoTbl.setModel(table_model)
        self.infoTbl.clicked.connect(self.showSelection)
        # enable sorting
        self.infoTbl.setSortingEnabled(True)
        """
    def retranslateUi(self, Mwindow):
        _translate = QCoreApplication.translate
        Mwindow.setWindowTitle(_translate("Mwin", "zxF"))
        self.chkBtn.setText(_translate("Mwin", "OK"))
        self.docBtn.setText(_translate("Mwin", "o"))
        self.recBtn.setText(_translate("Mwin", "k"))

class MyTableModel(QAbstractTableModel):
    """
    keep the method names
    they are an integral part of the model
    """

    def __init__(self, parent, mylist, header, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.mylist = mylist
        self.header = header


    def rowCount(self, parent):
        return len(self.mylist)

    def columnCount(self, parent):
        return len(self.mylist[0])  # return len(self.mylist[0])

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.mylist[index.row()][index.column()]

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None

    """
    def sort(self, col, order):
        #sort table by given column number col
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.mylist = sorted(self.mylist,
                             key=operator.itemgetter(col))
        if order == Qt.DescendingOrder:
            self.mylist.reverse()
        self.emit(SIGNAL("layoutChanged()"))
    """

    # you could process a CSV file to create this data


excel_path = '/home/zxf/病人登记/登记表.xlsx'
Df_data = pd.read_excel(excel_path)

data_l = np.array(Df_data)
# data_l.columns =['','','','','','','','','','','']
# Df_data.columns = ['id', 'RTid', 'Names', 'sex', 'age', 'Department', 'bedNum','dignose', 'phoneNum', 'bodyPart', 'startDate']
Df_header = ['id', 'RTid', 'Curesta', 'Names', 'sex', 'age', 'Department', 'bedNum',
             'dignose', 'phoneNum', 'bodyPart', 'startDate']

app = QApplication([])
# sys.argv
MainWindow = QMainWindow()
ui = Ui_Form(MainWindow,data_l,Df_header)
# ui.setupUi(MainWindow)
# MainWindow.setWindowIcon(QIcon('icon.png'))  #增加icon图标
# MainWindow.show()
ui.show()
sys.exit(app.exec_())