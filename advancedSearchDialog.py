# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'advancedSearchDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(666, 495)
        self.advTableComboBox = QtWidgets.QComboBox(Dialog)
        self.advTableComboBox.setGeometry(QtCore.QRect(70, 330, 181, 26))
        self.advTableComboBox.setObjectName("advTableComboBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 300, 91, 16))
        self.label.setObjectName("label")
        self.advSelectTableButton = QtWidgets.QPushButton(Dialog)
        self.advSelectTableButton.setGeometry(QtCore.QRect(290, 330, 31, 32))
        self.advSelectTableButton.setObjectName("advSelectTableButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(357, 300, 101, 16))
        self.label_2.setObjectName("label_2")
        self.advColumnComboBox = QtWidgets.QComboBox(Dialog)
        self.advColumnComboBox.setGeometry(QtCore.QRect(350, 330, 171, 26))
        self.advColumnComboBox.setObjectName("advColumnComboBox")
        self.advDoneButton = QtWidgets.QPushButton(Dialog)
        self.advDoneButton.setGeometry(QtCore.QRect(60, 400, 113, 32))
        self.advDoneButton.setObjectName("advDoneButton")
        self.advAddButton = QtWidgets.QPushButton(Dialog)
        self.advAddButton.setGeometry(QtCore.QRect(410, 400, 113, 32))
        self.advAddButton.setObjectName("advAddButton")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 30, 91, 16))
        self.label_5.setObjectName("label_5")
        self.searchPlaces = QtWidgets.QTableWidget(Dialog)
        self.searchPlaces.setGeometry(QtCore.QRect(140, 30, 431, 201))
        self.searchPlaces.setObjectName("searchPlaces")
        self.searchPlaces.setColumnCount(0)
        self.searchPlaces.setRowCount(0)
        self.advClearButton = QtWidgets.QPushButton(Dialog)
        self.advClearButton.setGeometry(QtCore.QRect(450, 240, 113, 32))
        self.advClearButton.setObjectName("advClearButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Select a Table"))
        self.advSelectTableButton.setText(_translate("Dialog", ">"))
        self.label_2.setText(_translate("Dialog", "Select a column"))
        self.advDoneButton.setText(_translate("Dialog", "Done"))
        self.advAddButton.setText(_translate("Dialog", "Add"))
        self.label_5.setText(_translate("Dialog", "Searching in:"))
        self.advClearButton.setText(_translate("Dialog", "Clear"))


