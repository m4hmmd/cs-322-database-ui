# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1016, 727)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 991, 651))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.closeConnectionButton = QtWidgets.QPushButton(self.tab_1)
        self.closeConnectionButton.setGeometry(QtCore.QRect(850, 70, 113, 32))
        self.closeConnectionButton.setObjectName("closeConnectionButton")
        self.tableComboBox = QtWidgets.QComboBox(self.tab_1)
        self.tableComboBox.setGeometry(QtCore.QRect(10, 40, 181, 31))
        self.tableComboBox.setObjectName("tableComboBox")
        self.label = QtWidgets.QLabel(self.tab_1)
        self.label.setGeometry(QtCore.QRect(10, 10, 171, 31))
        self.label.setObjectName("label")
        self.findTableButton = QtWidgets.QPushButton(self.tab_1)
        self.findTableButton.setGeometry(QtCore.QRect(10, 70, 113, 32))
        self.findTableButton.setObjectName("findTableButton")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_1)
        self.scrollArea.setGeometry(QtCore.QRect(20, 140, 941, 471))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 939, 469))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.mainTableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.mainTableWidget.setGeometry(QtCore.QRect(0, 0, 941, 471))
        self.mainTableWidget.setObjectName("mainTableWidget")
        self.mainTableWidget.setColumnCount(0)
        self.mainTableWidget.setRowCount(0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_2 = QtWidgets.QLabel(self.tab_1)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 171, 31))
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea_2.setGeometry(QtCore.QRect(20, 140, 721, 471))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 719, 469))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.mainTableWidget_2 = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_2)
        self.mainTableWidget_2.setGeometry(QtCore.QRect(0, 0, 721, 471))
        self.mainTableWidget_2.setObjectName("mainTableWidget_2")
        self.mainTableWidget_2.setColumnCount(0)
        self.mainTableWidget_2.setRowCount(0)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.searchBox = QtWidgets.QLineEdit(self.tab_2)
        self.searchBox.setGeometry(QtCore.QRect(10, 40, 371, 21))
        self.searchBox.setObjectName("searchBox")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 161, 21))
        self.label_3.setObjectName("label_3")
        self.searchButton = QtWidgets.QPushButton(self.tab_2)
        self.searchButton.setGeometry(QtCore.QRect(10, 70, 113, 32))
        self.searchButton.setObjectName("searchButton")
        self.scrollAreaTablesToSearch = QtWidgets.QScrollArea(self.tab_2)
        self.scrollAreaTablesToSearch.setGeometry(QtCore.QRect(760, 10, 201, 601))
        self.scrollAreaTablesToSearch.setWidgetResizable(True)
        self.scrollAreaTablesToSearch.setObjectName("scrollAreaTablesToSearch")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 199, 599))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label_4.setObjectName("label_4")
        self.scrollAreaTablesToSearch.setWidget(self.scrollAreaWidgetContents_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.advance_search_tab = QtWidgets.QWidget()
        self.advance_search_tab.setObjectName("advance_search_tab")
        self.advancedSearchScrollArea = QtWidgets.QScrollArea(self.advance_search_tab)
        self.advancedSearchScrollArea.setGeometry(QtCore.QRect(20, 140, 941, 471))
        self.advancedSearchScrollArea.setWidgetResizable(True)
        self.advancedSearchScrollArea.setObjectName("advancedSearchScrollArea")
        self.advancedSearchScrollAreaWidgetContents = QtWidgets.QWidget()
        self.advancedSearchScrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 939, 469))
        self.advancedSearchScrollAreaWidgetContents.setObjectName("advancedSearchScrollAreaWidgetContents")
        self.advMainTableWidget = QtWidgets.QTableWidget(self.advancedSearchScrollAreaWidgetContents)
        self.advMainTableWidget.setGeometry(QtCore.QRect(0, 0, 941, 471))
        self.advMainTableWidget.setObjectName("advMainTableWidget")
        self.advMainTableWidget.setColumnCount(0)
        self.advMainTableWidget.setRowCount(0)
        self.advancedSearchScrollArea.setWidget(self.advancedSearchScrollAreaWidgetContents)
        self.advancedSearchBox = QtWidgets.QLineEdit(self.advance_search_tab)
        self.advancedSearchBox.setGeometry(QtCore.QRect(10, 40, 371, 21))
        self.advancedSearchBox.setObjectName("advancedSearchBox")
        self.label_31 = QtWidgets.QLabel(self.advance_search_tab)
        self.label_31.setGeometry(QtCore.QRect(10, 10, 161, 21))
        self.label_31.setObjectName("label_31")
        self.advancedSearchButton = QtWidgets.QPushButton(self.advance_search_tab)
        self.advancedSearchButton.setGeometry(QtCore.QRect(10, 70, 113, 32))
        self.advancedSearchButton.setObjectName("advancedSearchButton")
        self.addSearchDetailsButton = QtWidgets.QPushButton(self.advance_search_tab)
        self.addSearchDetailsButton.setGeometry(QtCore.QRect(250, 70, 113, 32))
        self.addSearchDetailsButton.setObjectName("addSearchDetailsButton")
        self.tabWidget.addTab(self.advance_search_tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableComboBox_tab3 = QtWidgets.QComboBox(self.tab_3)
        self.tableComboBox_tab3.setGeometry(QtCore.QRect(10, 40, 181, 31))
        self.tableComboBox_tab3.setObjectName("tableComboBox_tab3")
        self.chooseATableLabel = QtWidgets.QLabel(self.tab_3)
        self.chooseATableLabel.setGeometry(QtCore.QRect(10, 10, 211, 31))
        self.chooseATableLabel.setObjectName("chooseATableLabel")
        self.showInputBarsButton = QtWidgets.QPushButton(self.tab_3)
        self.showInputBarsButton.setGeometry(QtCore.QRect(10, 70, 113, 32))
        self.showInputBarsButton.setObjectName("showInputBarsButton")
        self.scrollArea_tab3 = QtWidgets.QScrollArea(self.tab_3)
        self.scrollArea_tab3.setGeometry(QtCore.QRect(20, 140, 941, 471))
        self.scrollArea_tab3.setWidgetResizable(True)
        self.scrollArea_tab3.setObjectName("scrollArea_tab3")
        self.scrollAreaWidgetContents1 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents1.setGeometry(QtCore.QRect(0, 0, 939, 469))
        self.scrollAreaWidgetContents1.setObjectName("scrollAreaWidgetContents1")
        self.scrollArea_tab3.setWidget(self.scrollAreaWidgetContents1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.deleteTableComboBox = QtWidgets.QComboBox(self.tab_4)
        self.deleteTableComboBox.setGeometry(QtCore.QRect(10, 40, 181, 31))
        self.deleteTableComboBox.setObjectName("deleteTableComboBox")
        self.chooseATableLabel1 = QtWidgets.QLabel(self.tab_4)
        self.chooseATableLabel1.setGeometry(QtCore.QRect(10, 10, 231, 31))
        self.chooseATableLabel1.setObjectName("chooseATableLabel1")
        self.scrollArea_tab4 = QtWidgets.QScrollArea(self.tab_4)
        self.scrollArea_tab4.setGeometry(QtCore.QRect(20, 140, 941, 471))
        self.scrollArea_tab4.setWidgetResizable(True)
        self.scrollArea_tab4.setObjectName("scrollArea_tab4")
        self.scrollAreaWidgetContents2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents2.setGeometry(QtCore.QRect(0, 0, 939, 469))
        self.scrollAreaWidgetContents2.setObjectName("scrollAreaWidgetContents2")
        self.scrollArea_tab4.setWidget(self.scrollAreaWidgetContents2)
        self.deleteSelectTableButton = QtWidgets.QPushButton(self.tab_4)
        self.deleteSelectTableButton.setGeometry(QtCore.QRect(10, 70, 113, 32))
        self.deleteSelectTableButton.setObjectName("deleteSelectTableButton")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.scrollArea_tab5 = QtWidgets.QScrollArea(self.tab_5)
        self.scrollArea_tab5.setGeometry(QtCore.QRect(20, 140, 941, 471))
        self.scrollArea_tab5.setWidgetResizable(True)
        self.scrollArea_tab5.setObjectName("scrollArea_tab5")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 939, 469))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.predefinedMainTableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_4)
        self.predefinedMainTableWidget.setGeometry(QtCore.QRect(0, 0, 941, 471))
        self.predefinedMainTableWidget.setObjectName("predefinedMainTableWidget")
        self.predefinedMainTableWidget.setColumnCount(0)
        self.predefinedMainTableWidget.setRowCount(0)
        self.scrollArea_tab5.setWidget(self.scrollAreaWidgetContents_4)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_5)
        self.tabWidget_2.setGeometry(QtCore.QRect(20, 0, 941, 131))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.predefinedQueryTab_D2Q1 = QtWidgets.QWidget()
        self.predefinedQueryTab_D2Q1.setObjectName("predefinedQueryTab_D2Q1")
        self.label_5 = QtWidgets.QLabel(self.predefinedQueryTab_D2Q1)
        self.label_5.setGeometry(QtCore.QRect(260, 20, 261, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.predefinedQueryTab_D2Q1)
        self.label_6.setGeometry(QtCore.QRect(590, 20, 81, 16))
        self.label_6.setObjectName("label_6")
        self.spinBoxD2Q1 = QtWidgets.QSpinBox(self.predefinedQueryTab_D2Q1)
        self.spinBoxD2Q1.setGeometry(QtCore.QRect(530, 20, 48, 24))
        self.spinBoxD2Q1.setBaseSize(QtCore.QSize(11, 0))
        self.spinBoxD2Q1.setObjectName("spinBoxD2Q1")
        self.predefinedQueryButtonD2Q1 = QtWidgets.QPushButton(self.predefinedQueryTab_D2Q1)
        self.predefinedQueryButtonD2Q1.setGeometry(QtCore.QRect(410, 60, 113, 32))
        self.predefinedQueryButtonD2Q1.setObjectName("predefinedQueryButtonD2Q1")
        self.tabWidget_2.addTab(self.predefinedQueryTab_D2Q1, "")
        self.predefinedQueryTab_D2Q2 = QtWidgets.QWidget()
        self.predefinedQueryTab_D2Q2.setObjectName("predefinedQueryTab_D2Q2")
        self.label_7 = QtWidgets.QLabel(self.predefinedQueryTab_D2Q2)
        self.label_7.setGeometry(QtCore.QRect(490, 20, 211, 20))
        self.label_7.setObjectName("label_7")
        self.predefinedQueryButtonD2Q2 = QtWidgets.QPushButton(self.predefinedQueryTab_D2Q2)
        self.predefinedQueryButtonD2Q2.setGeometry(QtCore.QRect(410, 60, 113, 32))
        self.predefinedQueryButtonD2Q2.setObjectName("predefinedQueryButtonD2Q2")
        self.label_8 = QtWidgets.QLabel(self.predefinedQueryTab_D2Q2)
        self.label_8.setGeometry(QtCore.QRect(250, 20, 131, 16))
        self.label_8.setObjectName("label_8")
        self.comboBoxD2Q2 = QtWidgets.QComboBox(self.predefinedQueryTab_D2Q2)
        self.comboBoxD2Q2.setGeometry(QtCore.QRect(380, 20, 101, 26))
        self.comboBoxD2Q2.setObjectName("comboBoxD2Q2")
        self.tabWidget_2.addTab(self.predefinedQueryTab_D2Q2, "")
        self.predefinedQueryTab_D2Q3 = QtWidgets.QWidget()
        self.predefinedQueryTab_D2Q3.setObjectName("predefinedQueryTab_D2Q3")
        self.predefinedQueryButtonD2Q3 = QtWidgets.QPushButton(self.predefinedQueryTab_D2Q3)
        self.predefinedQueryButtonD2Q3.setGeometry(QtCore.QRect(410, 60, 113, 32))
        self.predefinedQueryButtonD2Q3.setObjectName("predefinedQueryButtonD2Q3")
        self.label_10 = QtWidgets.QLabel(self.predefinedQueryTab_D2Q3)
        self.label_10.setGeometry(QtCore.QRect(120, 20, 391, 16))
        self.label_10.setObjectName("label_10")
        self.comboBoxD2Q3_start = QtWidgets.QComboBox(self.predefinedQueryTab_D2Q3)
        self.comboBoxD2Q3_start.setGeometry(QtCore.QRect(510, 20, 141, 26))
        self.comboBoxD2Q3_start.setObjectName("comboBoxD2Q3_start")
        self.label_20 = QtWidgets.QLabel(self.predefinedQueryTab_D2Q3)
        self.label_20.setGeometry(QtCore.QRect(660, 20, 21, 16))
        self.label_20.setObjectName("label_20")
        self.comboBoxD2Q3_end = QtWidgets.QComboBox(self.predefinedQueryTab_D2Q3)
        self.comboBoxD2Q3_end.setGeometry(QtCore.QRect(690, 20, 141, 26))
        self.comboBoxD2Q3_end.setObjectName("comboBoxD2Q3_end")
        self.tabWidget_2.addTab(self.predefinedQueryTab_D2Q3, "")
        self.predefinedQueryTab_D2Q4 = QtWidgets.QWidget()
        self.predefinedQueryTab_D2Q4.setObjectName("predefinedQueryTab_D2Q4")
        self.predefinedQueryButtonD2Q4 = QtWidgets.QPushButton(self.predefinedQueryTab_D2Q4)
        self.predefinedQueryButtonD2Q4.setGeometry(QtCore.QRect(410, 60, 113, 32))
        self.predefinedQueryButtonD2Q4.setObjectName("predefinedQueryButtonD2Q4")
        self.label_11 = QtWidgets.QLabel(self.predefinedQueryTab_D2Q4)
        self.label_11.setGeometry(QtCore.QRect(140, 20, 651, 31))
        self.label_11.setObjectName("label_11")
        self.tabWidget_2.addTab(self.predefinedQueryTab_D2Q4, "")
        self.predefinedQueryTab_D2Q5 = QtWidgets.QWidget()
        self.predefinedQueryTab_D2Q5.setObjectName("predefinedQueryTab_D2Q5")
        self.label_12 = QtWidgets.QLabel(self.predefinedQueryTab_D2Q5)
        self.label_12.setGeometry(QtCore.QRect(260, 20, 461, 31))
        self.label_12.setObjectName("label_12")
        self.predefinedQueryButtonD2Q5 = QtWidgets.QPushButton(self.predefinedQueryTab_D2Q5)
        self.predefinedQueryButtonD2Q5.setGeometry(QtCore.QRect(410, 60, 113, 32))
        self.predefinedQueryButtonD2Q5.setObjectName("predefinedQueryButtonD2Q5")
        self.tabWidget_2.addTab(self.predefinedQueryTab_D2Q5, "")
        self.predefinedQueryTab_D2Q6 = QtWidgets.QWidget()
        self.predefinedQueryTab_D2Q6.setObjectName("predefinedQueryTab_D2Q6")
        self.predefinedQueryButtonD2Q6 = QtWidgets.QPushButton(self.predefinedQueryTab_D2Q6)
        self.predefinedQueryButtonD2Q6.setGeometry(QtCore.QRect(410, 60, 113, 32))
        self.predefinedQueryButtonD2Q6.setObjectName("predefinedQueryButtonD2Q6")
        self.label_13 = QtWidgets.QLabel(self.predefinedQueryTab_D2Q6)
        self.label_13.setGeometry(QtCore.QRect(270, 20, 311, 31))
        self.label_13.setObjectName("label_13")
        self.label_9 = QtWidgets.QLabel(self.predefinedQueryTab_D2Q6)
        self.label_9.setGeometry(QtCore.QRect(650, 30, 71, 16))
        self.label_9.setObjectName("label_9")
        self.spinBoxD2Q6 = QtWidgets.QSpinBox(self.predefinedQueryTab_D2Q6)
        self.spinBoxD2Q6.setGeometry(QtCore.QRect(590, 20, 48, 24))
        self.spinBoxD2Q6.setObjectName("spinBoxD2Q6")
        self.tabWidget_2.addTab(self.predefinedQueryTab_D2Q6, "")
        self.predefinedQueryTab_D2Q7 = QtWidgets.QWidget()
        self.predefinedQueryTab_D2Q7.setObjectName("predefinedQueryTab_D2Q7")
        self.label_14 = QtWidgets.QLabel(self.predefinedQueryTab_D2Q7)
        self.label_14.setGeometry(QtCore.QRect(160, 20, 461, 31))
        self.label_14.setObjectName("label_14")
        self.predefinedQueryButtonD2Q7 = QtWidgets.QPushButton(self.predefinedQueryTab_D2Q7)
        self.predefinedQueryButtonD2Q7.setGeometry(QtCore.QRect(410, 60, 113, 32))
        self.predefinedQueryButtonD2Q7.setObjectName("predefinedQueryButtonD2Q7")
        self.comboBoxD2Q7 = QtWidgets.QComboBox(self.predefinedQueryTab_D2Q7)
        self.comboBoxD2Q7.setGeometry(QtCore.QRect(590, 20, 191, 26))
        self.comboBoxD2Q7.setObjectName("comboBoxD2Q7")
        self.tabWidget_2.addTab(self.predefinedQueryTab_D2Q7, "")
        self.predefinedQueryTab_D2Q8 = QtWidgets.QWidget()
        self.predefinedQueryTab_D2Q8.setObjectName("predefinedQueryTab_D2Q8")
        self.predefinedQueryButtonD2Q8 = QtWidgets.QPushButton(self.predefinedQueryTab_D2Q8)
        self.predefinedQueryButtonD2Q8.setGeometry(QtCore.QRect(410, 60, 113, 32))
        self.predefinedQueryButtonD2Q8.setObjectName("predefinedQueryButtonD2Q8")
        self.label_15 = QtWidgets.QLabel(self.predefinedQueryTab_D2Q8)
        self.label_15.setGeometry(QtCore.QRect(160, 20, 311, 31))
        self.label_15.setObjectName("label_15")
        self.label_18 = QtWidgets.QLabel(self.predefinedQueryTab_D2Q8)
        self.label_18.setGeometry(QtCore.QRect(540, 20, 291, 16))
        self.label_18.setObjectName("label_18")
        self.spinBoxD2Q8 = QtWidgets.QSpinBox(self.predefinedQueryTab_D2Q8)
        self.spinBoxD2Q8.setGeometry(QtCore.QRect(480, 20, 48, 24))
        self.spinBoxD2Q8.setBaseSize(QtCore.QSize(11, 0))
        self.spinBoxD2Q8.setObjectName("spinBoxD2Q8")
        self.tabWidget_2.addTab(self.predefinedQueryTab_D2Q8, "")
        self.predefinedQueryTab_D2Q9 = QtWidgets.QWidget()
        self.predefinedQueryTab_D2Q9.setObjectName("predefinedQueryTab_D2Q9")
        self.predefinedQueryButtonD2Q9 = QtWidgets.QPushButton(self.predefinedQueryTab_D2Q9)
        self.predefinedQueryButtonD2Q9.setGeometry(QtCore.QRect(410, 60, 113, 32))
        self.predefinedQueryButtonD2Q9.setObjectName("predefinedQueryButtonD2Q9")
        self.label_16 = QtWidgets.QLabel(self.predefinedQueryTab_D2Q9)
        self.label_16.setGeometry(QtCore.QRect(140, 20, 511, 31))
        self.label_16.setObjectName("label_16")
        self.comboBoxD2Q9 = QtWidgets.QComboBox(self.predefinedQueryTab_D2Q9)
        self.comboBoxD2Q9.setGeometry(QtCore.QRect(650, 20, 161, 26))
        self.comboBoxD2Q9.setObjectName("comboBoxD2Q9")
        self.tabWidget_2.addTab(self.predefinedQueryTab_D2Q9, "")
        self.predefinedQueryTab_D2Q10 = QtWidgets.QWidget()
        self.predefinedQueryTab_D2Q10.setObjectName("predefinedQueryTab_D2Q10")
        self.predefinedQueryButtonD2Q10 = QtWidgets.QPushButton(self.predefinedQueryTab_D2Q10)
        self.predefinedQueryButtonD2Q10.setGeometry(QtCore.QRect(410, 60, 113, 32))
        self.predefinedQueryButtonD2Q10.setObjectName("predefinedQueryButtonD2Q10")
        self.label_17 = QtWidgets.QLabel(self.predefinedQueryTab_D2Q10)
        self.label_17.setGeometry(QtCore.QRect(130, 20, 261, 31))
        self.label_17.setObjectName("label_17")
        self.comboBoxD2Q10_c = QtWidgets.QComboBox(self.predefinedQueryTab_D2Q10)
        self.comboBoxD2Q10_c.setGeometry(QtCore.QRect(670, 20, 161, 26))
        self.comboBoxD2Q10_c.setObjectName("comboBoxD2Q10_c")
        self.comboBoxD2Q10_pt = QtWidgets.QComboBox(self.predefinedQueryTab_D2Q10)
        self.comboBoxD2Q10_pt.setGeometry(QtCore.QRect(410, 20, 161, 26))
        self.comboBoxD2Q10_pt.setObjectName("comboBoxD2Q10_pt")
        self.label_19 = QtWidgets.QLabel(self.predefinedQueryTab_D2Q10)
        self.label_19.setGeometry(QtCore.QRect(580, 20, 81, 16))
        self.label_19.setObjectName("label_19")
        self.tabWidget_2.addTab(self.predefinedQueryTab_D2Q10, "")
        self.tabWidget.addTab(self.tab_5, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.closeConnectionButton.setText(_translate("MainWindow", "Disconnect"))
        self.label.setText(_translate("MainWindow", "Choose a table to access"))
        self.findTableButton.setText(_translate("MainWindow", "Find Table"))
        self.label_2.setText(_translate("MainWindow", "Ouptut:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Print Tables"))
        self.label_3.setText(_translate("MainWindow", "Enter a keyword to search:"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.label_4.setText(_translate("MainWindow", "Tables to Search (optional)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Search"))
        self.label_31.setText(_translate("MainWindow", "Enter a keyword to search:"))
        self.advancedSearchButton.setText(_translate("MainWindow", "Search"))
        self.addSearchDetailsButton.setText(_translate("MainWindow", "Advanced"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.advance_search_tab), _translate("MainWindow", "Advanced"))
        self.chooseATableLabel.setText(_translate("MainWindow", "Choose a table to insert values to"))
        self.showInputBarsButton.setText(_translate("MainWindow", "Next"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Insert"))
        self.chooseATableLabel1.setText(_translate("MainWindow", "Choose a table to delete a tuple from"))
        self.deleteSelectTableButton.setText(_translate("MainWindow", "Next"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Delete"))
        self.label_5.setText(_translate("MainWindow", "What is the average price for a listing with"))
        self.label_6.setText(_translate("MainWindow", "bedrooms?"))
        self.predefinedQueryButtonD2Q1.setText(_translate("MainWindow", "Search"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.predefinedQueryTab_D2Q1), _translate("MainWindow", "D2Q1"))
        self.label_7.setText(_translate("MainWindow", "review score for listings with TV?"))
        self.predefinedQueryButtonD2Q2.setText(_translate("MainWindow", "Search"))
        self.label_8.setText(_translate("MainWindow", "What is the average "))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.predefinedQueryTab_D2Q2), _translate("MainWindow", "D2Q2"))
        self.predefinedQueryButtonD2Q3.setText(_translate("MainWindow", "Search"))
        self.label_10.setText(_translate("MainWindow", "Print all the hosts who have an available property between date"))
        self.label_20.setText(_translate("MainWindow", "and"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.predefinedQueryTab_D2Q3), _translate("MainWindow", "D2Q3"))
        self.predefinedQueryButtonD2Q4.setText(_translate("MainWindow", "Search"))
        self.label_11.setText(_translate("MainWindow", "Print how many listing items exist that are posted by two different hosts but the hosts have the same name."))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.predefinedQueryTab_D2Q4), _translate("MainWindow", "D2Q4"))
        self.label_12.setText(_translate("MainWindow", "Print all the dates that \'Viajes Eco\' has available accommodations for rent."))
        self.predefinedQueryButtonD2Q5.setText(_translate("MainWindow", "Search"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.predefinedQueryTab_D2Q5), _translate("MainWindow", "D2Q5"))
        self.predefinedQueryButtonD2Q6.setText(_translate("MainWindow", "Search"))
        self.label_13.setText(_translate("MainWindow", "Find all the hosts (host_ids, host_names) that have"))
        self.label_9.setText(_translate("MainWindow", "listing(s)."))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.predefinedQueryTab_D2Q6), _translate("MainWindow", "D2Q6"))
        self.label_14.setText(_translate("MainWindow", "What is the difference in the average price of listings with and without"))
        self.predefinedQueryButtonD2Q7.setText(_translate("MainWindow", "Search"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.predefinedQueryTab_D2Q7), _translate("MainWindow", "D2Q7"))
        self.predefinedQueryButtonD2Q8.setText(_translate("MainWindow", "Search"))
        self.label_15.setText(_translate("MainWindow", "How much more (or less) costly to rent a room with"))
        self.label_18.setText(_translate("MainWindow", "beds in Berlin compared to Madrid on average?"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.predefinedQueryTab_D2Q8), _translate("MainWindow", "D2Q8"))
        self.predefinedQueryButtonD2Q9.setText(_translate("MainWindow", "Search"))
        self.label_16.setText(_translate("MainWindow", "Find the top-10 (in terms of the number of listings) hosts (host_ids, host_names) in"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.predefinedQueryTab_D2Q9), _translate("MainWindow", "D2Q9"))
        self.predefinedQueryButtonD2Q10.setText(_translate("MainWindow", "Search"))
        self.label_17.setText(_translate("MainWindow", "Find the top-10 rated (review_score_rating)"))
        self.label_19.setText(_translate("MainWindow", " (id,name) in"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.predefinedQueryTab_D2Q10), _translate("MainWindow", "D2Q10"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Predefined"))


