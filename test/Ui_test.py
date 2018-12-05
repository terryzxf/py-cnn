#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we create a bit
more complicated window layout using
the QGridLayout manager.

author: Jan Bodnar
website: zetcode.com
last edited: January 2015
"""


"""
import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QTextEdit, QGridLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    
"""

import operator  # used for sorting
from PyQt5.QtWidgets import QWidget, QApplication, QTableView, QVBoxLayout #QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication)
from PyQt5.QtCore import QAbstractTableModel, Qt
#from PyQt5.QtGui import *
import pandas as pd
import numpy as np


class MyWindow(QWidget):
    def __init__(self, dataList, header, *args):
        QWidget.__init__(self, *args)
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(70, 150, 420, 250)
        self.setWindowTitle("Click on the header to sort table")

        table_model = MyTableModel(self, dataList, header)
        table_view = QTableView()
        # bind cell click to a method reference
        table_view.clicked.connect(self.showSelection)

        table_view.setModel(table_model)
        # enable sorting
        table_view.setSortingEnabled(True)

        layout = QVBoxLayout(self)
        layout.addWidget(table_view)
        self.setLayout(layout)

    def showSelection(self, item):
        cellContent = item.data()
        print(cellContent)  # test
        sf= "  {}  选中 ".format(cellContent)#sf = "You clicked on {}".format(cellContent)
        # display in title bar for convenience
        self.setWindowTitle(sf)


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
        return len(self.mylist[0])       #return len(self.mylist[0])

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

excel_path='/home/zxf/病人登记/登记表.xlsx'
Df_data = pd.read_excel(excel_path)

data_l =np.array(Df_data)
#data_l.columns =['','','','','','','','','','','']
#Df_data.columns = ['id', 'RTid', 'Names', 'sex', 'age', 'Department', 'bedNum','dignose', 'phoneNum', 'bodyPart', 'startDate']
Df_header = ['id', 'RTid', 'Curesta', 'Names', 'sex', 'age', 'Department', 'bedNum',
                   'dignose', 'phoneNum', 'bodyPart', 'startDate']

#header = ['First Name', 'Last Name', 'Age', 'Weight']

# a list of (fname, lname, age, weight) tuples

"""
dataList = [
    ('Ben', 'Dover', 36, 127),
    ('Foster', 'Krampf', 27, 234),
    ('Barry', 'Chaurus', 19, 315),
    ('Sede', 'Anowski', 59, 147),
    ('Carolus', 'Gabel', 94, 102),
    ('Michel', 'Zittus', 21, 175),
    ('Annie', 'Waters', 31, 114)
]


"""
#print('@@@@@@@@@@@@@@@@@@@@@@@@')
#print(Df_header)
#print(len(data_l.index))
#"""
app = QApplication([])
win = MyWindow(data_l,Df_header)
#win = MyWindow(dataList, header)
win.show()
app.exec_()

#"""