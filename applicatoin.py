import sys
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QPushButton, QWidget
from PyQt5.QtWidgets import QMainWindow, QCheckBox, QLineEdit, QLabel
from PyQt5 import QtCore
import cx_Oracle

from mainWindow import Ui_MainWindow

all_table_names = ['Has_Cities', 'Countries']

def get_table_names():
    # c = conn.cursor()
    query = 'SELECT table_name FROM user_tables'
    c.execute(query)
    global all_table_names
    all_table_names = sorted([x[0] for x in c.fetchall()])

class MainWindow:

    def __init__(self):

        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.populate_table_names()
        self.populate_table_checkboxes()
        self.ui.tableSubmitButton.clicked.connect(self.show_table)
        self.ui.tableSubmitButton_tab3.clicked.connect(self.create_insert_form)
        self.ui.closeConnectionButton.clicked.connect(self.close_connection)
        self.ui.searchButton.clicked.connect(self.search_keyword)

    def show(self):

        self.main_win.show()

    def populate_table_names(self):
        self.ui.tableComboBox.addItems(all_table_names)
        self.ui.tableComboBox_tab3.addItems(all_table_names)

    def get_column_names(self, table_name):
        query = "SELECT column_name FROM all_tab_columns WHERE TABLE_NAME = '" + table_name + "'"
        c.execute(query)
        return [x[0] for x in c.fetchall()]

    def show_table(self):
        table_name = self.ui.tableComboBox.currentText()
        query = 'select * from ' + table_name

        # execute sql query
        c = conn.cursor()
        result = c.execute(query)

        # find column headers
        col_names = self.get_column_names(table_name)
        column_count = len(col_names)

        # init table
        self.ui.mainTableWidget.setColumnCount(column_count)
        self.ui.mainTableWidget.setRowCount(0)
        self.ui.mainTableWidget.setHorizontalHeaderLabels(col_names)

        # fill table
        for row_number, row_data in enumerate(result):
            self.ui.mainTableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.mainTableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def search_keyword(self):
        keyword = self.ui.searchBox.text()
        tables_to_search = [all_table_names[i] for i, checkBox in enumerate(self.ui.checkBoxes) if checkBox.isChecked()]

        print(keyword)
        print(tables_to_search)

        if len(tables_to_search) == 0:
            # basic search
            query = 'select * from Countries'  # TODO
        else:
            # advanced search
            query = 'select * from Countries'  # TODO

        # execute sql query
        c = conn.cursor()
        result = c.execute(query)

        column_count = 5 #TODO
        col_names = ['A', 'B', 'C', 'D', 'E'] #TODO

        # init table
        self.ui.mainTableWidget_2.setColumnCount(column_count)
        self.ui.mainTableWidget_2.setRowCount(0)
        self.ui.mainTableWidget_2.setHorizontalHeaderLabels(col_names)

        # fill table
        for row_number, row_data in enumerate(result):
            self.ui.mainTableWidget_2.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.mainTableWidget_2.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def populate_table_checkboxes(self):
        self.ui.checkBoxes = []
        for i, table_name in enumerate(all_table_names):
            checkBox = QCheckBox(self.ui.scrollAreaWidgetContents_3)
            checkBox.setGeometry(QtCore.QRect(10, 30 + i*20, 200, 20))
            checkBox.setObjectName("checkBox" + table_name)

            _translate = QtCore.QCoreApplication.translate
            checkBox.setText(_translate("MainWindow", table_name))
            self.ui.checkBoxes.append(checkBox)

    def create_insert_form(self):
        table_name = self.ui.tableComboBox_tab3.currentText()
        col_names = self.get_column_names(table_name)

        self.ui.scrollAreaWidgetContents1 = QWidget()
        self.ui.scrollAreaWidgetContents1.setGeometry(QtCore.QRect(0, 0, 939, 469))
        self.ui.scrollAreaWidgetContents1.setObjectName("scrollAreaWidgetContents1")

        # add labels and forms
        self.ui.insertLabels = []
        self.ui.insertLineEdits = []
        for i, col in enumerate(col_names):
            label = QLabel(self.ui.scrollAreaWidgetContents1)
            label.setGeometry(QtCore.QRect(10, 10 + i*25, 131, 20))
            label.setObjectName("insertLabel_" + str(i))

            _translate = QtCore.QCoreApplication.translate
            label.setText(_translate("MainWindow", col))

            self.ui.insertLabels.append(label)

            lineEdit = QLineEdit(self.ui.scrollAreaWidgetContents1)
            lineEdit.setGeometry(QtCore.QRect(170, 10 + i*25, 113, 25))
            lineEdit.setObjectName("insertLineEdit_" + str(i))
            self.ui.insertLineEdits.append(lineEdit)

        # add submit button
        self.ui.submitInsertButton = QPushButton(self.ui.scrollAreaWidgetContents1)
        self.ui.submitInsertButton.setGeometry(QtCore.QRect(20, 10 + 25 * len(col_names), 113, 32))
        self.ui.submitInsertButton.setObjectName("submitInsertButton")
        self.ui.submitInsertButton.setText(_translate("MainWindow", "Insert"))

        self.ui.submitInsertButton.clicked.connect(self.insert_into_tables)

        # add cancel button
        self.ui.cancelInsertButton = QPushButton(self.ui.scrollAreaWidgetContents1)
        self.ui.cancelInsertButton.setGeometry(QtCore.QRect(150, 10 + 25 * len(col_names), 113, 32))
        self.ui.cancelInsertButton.setObjectName("cancelInsertButton")
        self.ui.cancelInsertButton.setText(_translate("MainWindow", "Cancel"))

        self.ui.cancelInsertButton.clicked.connect(self.finish_insert)

        # add the whole content to scroll area
        self.ui.scrollArea_tab3.setWidget(self.ui.scrollAreaWidgetContents1)

    def insert_into_tables(self):
        # get column names and values
        table_name = self.ui.tableComboBox_tab3.currentText()
        col_names = self.get_column_names(table_name)
        values = [lineEdit.text() for lineEdit in self.ui.insertLineEdits]

        # construct query
        query = "INSERT INTO " + table_name + " ("
        for col_name in col_names[:-1]:
            query += col_name + ", "
        query += col_names[-1] + ") VALUES ("
        for value in values[:-1]:
            query += "'" + value + "', "
        query += "'" + values[-1] + "')"
        print(query)

        # insert
        c = conn.cursor()
        c.execute(query)
        conn.commit()

        self.finish_insert()

    def finish_insert(self):
        for label in self.ui.insertLabels:
            label.setParent(None)
        for lineEdit in self.ui.insertLineEdits:
            lineEdit.setParent(None)
        self.ui.cancelInsertButton.setParent(None)
        self.ui.submitInsertButton.setParent(None)
        self.ui.insertLabels = []
        self.ui.insertLineEdits = []
        self.ui.scrollAreaWidgetContents1.setParent(None)

    def close_connection(self):
        conn.close()

if __name__ == '__main__':
    dsn_tns = cx_Oracle.makedsn('cs322-db.epfl.ch', '1521', sid='ORCLCDB')
    conn = cx_Oracle.connect(user=r'C##DB2019_G48', password='DB2019_G48', dsn=dsn_tns)
    c = conn.cursor()


    get_table_names()


    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())