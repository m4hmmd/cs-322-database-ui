import sys
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QPushButton, QWidget, QScrollArea
from PyQt5.QtWidgets import QMainWindow, QCheckBox, QLineEdit, QLabel, QDialog, QTableWidget, QTabWidget
from PyQt5 import QtCore
from advancedSearchDialog import Ui_Dialog
import cx_Oracle

from mainWindow import Ui_MainWindow



class MainWindow:
    MAX_TUPLES_PER_PAGE = 1000
    places_to_search = set()  # gonna be a set of tuples (TABLE_NAME, COLUMN_NAME)
    prim_keys = {}
    _translate = QtCore.QCoreApplication.translate
    all_table_names = ['Has_Cities', 'Countries']
    all_amenities = ['Wifi', 'TV']
    all_property_types = ['Apartment']
    all_months_start = ['2018-11-07', '2018-12-01', '2019-01-01', '2019-02-01', '2019-03-01', '2019-04-01', '2019-05-01', '2019-06-01', '2019-07-01', '2019-08-01', '2019-09-01', '2019-10-01', '2019-11-01']
    all_months_end = ['2018-11-30', '2018-12-31', '2019-01-31', '2019-02-28', '2019-03-31', '2019-04-30', '2019-05-31', '2019-06-30', '2019-07-31', '2019-08-31', '2019-09-30', '2019-10-31', '2019-11-30']
    all_months = ['2018-11', '2018-12', '2019-01', '2019-02', '2019-03', '2019-04', '2019-05', '2019-06', '2019-07', '2019-08', '2019-09', '2019-10', '2019-11']
    default_places_to_search = {'AMENITIES': ['AMENITY_NAME'],
                                'BED_TYPES': ['BED_TYPE'],
                                'CANCELLATION_POLICIES': ['CANCELLATION_POLICY'],
                                'COUNTRIES': ['COUNTRY'],
                                'DATES': ['CAL_DATE'],
                                'HAS_AMENITIES': [],
                                'HAS_CITIES': ['CITY'],
                                'HAS_INFO': ['LISTING_NAME', 'SUMMARY_INFO', 'SPACE_INFO', 'NEIGHBORHOOD_OVERVIEW'], #TODO not DESCRIPTION; should it be here?
                                'HAS_NEIGHBOURHOODS': ['NEIGHBOURHOOD'],
                                'HAS_SCORES': [],
                                'HAS_VERIFICATIONS': [],
                                'HOST_RESPONSE_TIMES': [],
                                'HOSTS': [],
                                'LISTINGS': [],
                                'PRICES': [],
                                'PROPERTY_TYPES': ['PROPERTY_TYPE'],
                                'REVIEWED_BY': [],
                                'ROOM_TYPES': [],
                                'RULES': [],
                                'UI_TEST': [],
                                'VERIFICATIONS': []
                                }

    def __init__(self):
        dsn_tns = cx_Oracle.makedsn('cs322-db.epfl.ch', '1521', sid='ORCLCDB')
        self.conn = cx_Oracle.connect(user=r'C##DB2019_G48', password='DB2019_G48', dsn=dsn_tns)
        c = self.conn.cursor()

        self.get_table_names()
        self.get_primary_keys()
        self.get_all_amenities()
        self.get_all_property_types()


        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.populate_table_names()
        self.populate_table_checkboxes()

        # advanced search tab widget
        self.ui.searchTabWidget = QTabWidget(self.ui.tab_2)
        self.ui.searchTabWidget.setGeometry(QtCore.QRect(10, 99, 741, 511))
        self.ui.searchTabWidget.setObjectName("searchTabWidget")

        # buttons
        self.ui.findTableButton.clicked.connect(self.show_table)
        self.ui.showInputBarsButton.clicked.connect(self.create_insert_form)
        self.ui.closeConnectionButton.clicked.connect(self.close_connection)
        self.ui.searchButton.clicked.connect(self.search_keyword)
        self.ui.addSearchDetailsButton.clicked.connect(self.add_search_details)
        self.ui.advancedSearchButton.clicked.connect(self.advanced_search_keyword)
        self.ui.deleteSelectTableButton.clicked.connect(self.create_delete_forms)
        self.ui.printTablesMoreButton.clicked.connect(self.show_more)
        self.ui.advancedSearchMoreButton.clicked.connect(self.show_more_advanced_search)
        self.ui.searchMoreButton.clicked.connect(self.show_more_search)

        # predefined queries presets
        self.ui.spinBoxD2Q1.setValue(8)
        self.ui.comboBoxD2Q2.addItems(['accuracy', 'cleanliness', 'checkin', 'communication', 'location', 'value'])
        self.ui.comboBoxD2Q2.setCurrentText('cleanliness')
        self.ui.comboBoxD2Q3_start.addItems(self.all_months)
        self.ui.comboBoxD2Q3_end.addItems(self.all_months)
        self.ui.comboBoxD2Q3_start.setCurrentText('2019-03')
        self.ui.comboBoxD2Q3_end.setCurrentText('2019-09')
        self.ui.spinBoxD2Q6.setValue(1)
        self.ui.comboBoxD2Q7.addItems(self.all_amenities)
        self.ui.comboBoxD2Q7.setCurrentText('Wifi')
        self.ui.spinBoxD2Q8.setValue(8)
        self.ui.comboBoxD2Q9.setCurrentText('Spain')
        self.ui.comboBoxD2Q9.addItems(['Spain', 'Germany'])
        self.ui.comboBoxD2Q10_c.addItems(['Barcelona', 'Madrid', 'Berlin'])
        self.ui.comboBoxD2Q10_c.setCurrentText('Barcelona')
        self.ui.comboBoxD2Q10_pt.addItems(self.all_property_types)
        self.ui.comboBoxD2Q10_pt.setCurrentText('Apartment')

        # predefined query functions
        self.ui.predefinedQueryButtonD2Q1.clicked.connect(self.d1q1)
        self.ui.predefinedQueryButtonD2Q2.clicked.connect(self.d1q2)
        self.ui.predefinedQueryButtonD2Q3.clicked.connect(self.d1q3)
        self.ui.predefinedQueryButtonD2Q4.clicked.connect(self.d1q4)
        self.ui.predefinedQueryButtonD2Q5.clicked.connect(self.d1q5)
        self.ui.predefinedQueryButtonD2Q6.clicked.connect(self.d1q6)
        self.ui.predefinedQueryButtonD2Q7.clicked.connect(self.d1q7)
        self.ui.predefinedQueryButtonD2Q8.clicked.connect(self.d1q8)
        self.ui.predefinedQueryButtonD2Q9.clicked.connect(self.d1q9)
        self.ui.predefinedQueryButtonD2Q10.clicked.connect(self.d1q10)


    def show(self):
        self.main_win.show()

    def get_table_names(self):
        # c = conn.cursor()
        query = 'SELECT table_name FROM user_tables'
        c = self.conn.cursor()
        c.execute(query)
        self.all_table_names = sorted([x[0] for x in c.fetchall()])

    def get_primary_keys(self):
        # get primary key information
        for table_name in self.all_table_names:
            query = "SELECT cols.column_name \
                    FROM all_constraints cons, all_cons_columns cols \
                    WHERE cols.table_name = {} \
                    AND cons.constraint_type = 'P'\
                    AND cons.constraint_name = cols.constraint_name\
                    ORDER BY cols.table_name, cols.position".format("'" + table_name + "'")
            c = self.conn.cursor()
            c.execute(query)
            self.prim_keys[table_name] =[ x[0] for x in c.fetchall() ]

        print(self.prim_keys)

    def get_all_amenities(self):
        c = self.conn.cursor()
        c.execute("Select AMENITY_NAME from AMENITIES")
        self.all_amenities = [x[0] for x in c.fetchall()]

    def get_all_property_types(self):
        c = self.conn.cursor()
        c.execute("Select PROPERTY_TYPE from PROPERTY_TYPES")
        self.all_property_types = [x[0] for x in c.fetchall()]

    def populate_table_names(self):
        self.ui.tableComboBox.addItems(self.all_table_names)
        self.ui.tableComboBox_tab3.addItems(self.all_table_names)
        self.ui.deleteTableComboBox.addItems(self.all_table_names)

    def get_column_names(self, table_name):
        query = "SELECT column_name FROM all_tab_columns WHERE TABLE_NAME = '" + table_name + "'"
        c = self.conn.cursor()
        c.execute(query)
        return [x[0] for x in c.fetchall()]

    def show_table(self):
        table_name = self.ui.tableComboBox.currentText()
        query = 'select * from ' + table_name

        # execute sql query
        c = self.conn.cursor()
        result = c.execute(query)

        self.temp_table_print_tables = result
        self.temp_stop_print_tables = 0

        # find column headers
        col_names = self.get_column_names(table_name)
        column_count = len(col_names)

        # init table
        self.ui.mainTableWidget.setColumnCount(column_count)
        self.ui.mainTableWidget.setRowCount(0)
        self.ui.mainTableWidget.setHorizontalHeaderLabels(col_names)

        # fill table
        for row_number, row_data in enumerate(result):
            if row_number >= self.MAX_TUPLES_PER_PAGE:
                self.temp_stop_print_tables = self.MAX_TUPLES_PER_PAGE
                break

            self.ui.mainTableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.mainTableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))


    def show_more(self):
        # fill table
        for row_number, row_data in enumerate(self.temp_table_print_tables):
            if row_number >= self.MAX_TUPLES_PER_PAGE:
                self.temp_stop_print_tables += self.MAX_TUPLES_PER_PAGE
                break
            self.ui.mainTableWidget.insertRow(row_number + self.temp_stop_print_tables)
            for column_number, data in enumerate(row_data):
                self.ui.mainTableWidget.setItem(row_number + self.temp_stop_print_tables, column_number, QTableWidgetItem(str(data)))


    def advanced_search_keyword(self):
        keyword = self.ui.advancedSearchBox.text()
        keyword = keyword.replace("'", "''")
        query = ''
        places = list(self.places_to_search)
        if len(places) > 0:
            columns = [x[1] for x in places]
            table_name = places[0][0]
            query = 'SELECT * FROM ' + table_name + ' WHERE'
            query += ' OR '.join([' ' + col + " LIKE '%" + keyword + "%'" for col in columns])
            print(query)
            # execute sql query
            c = self.conn.cursor()
            result = c.execute(query)

            self.temp_table_advanced_search = result
            self.temp_stop_advanced_search = 0

            col_names = self.get_column_names(table_name)
            column_count = len(col_names)

            # init table
            self.ui.advMainTableWidget.setColumnCount(column_count)
            self.ui.advMainTableWidget.setRowCount(0)
            self.ui.advMainTableWidget.setHorizontalHeaderLabels(col_names)

            # fill table
            for row_number, row_data in enumerate(result):
                if row_number >= self.MAX_TUPLES_PER_PAGE:
                    self.temp_stop_advanced_search = self.MAX_TUPLES_PER_PAGE
                    break

                self.ui.advMainTableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.advMainTableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        else:
            # TODO display proper error msg
            print('Why use advanced search then?')

    def show_more_advanced_search(self):
        # fill table
        for row_number, row_data in enumerate(self.temp_table_advanced_search):
            if row_number >= self.MAX_TUPLES_PER_PAGE:
                self.temp_stop_advanced_search += self.MAX_TUPLES_PER_PAGE
                break
            self.ui.advMainTableWidget.insertRow(row_number + self.temp_stop_advanced_search)
            for column_number, data in enumerate(row_data):
                self.ui.advMainTableWidget.setItem(row_number + self.temp_stop_advanced_search, column_number, QTableWidgetItem(str(data)))

    def search_keyword(self):
        self.ui.searchTabWidget.clear()

        keyword = self.ui.searchBox.text()
        keyword = keyword.replace("'", "''")
        non_empty_table_names = [table_name for table_name in self.all_table_names if len(self.default_places_to_search[table_name]) != 0]
        tables_to_search = [non_empty_table_names[i] for i, checkBox in enumerate(self.ui.checkBoxes) if
                            checkBox.isChecked()]

        if len(tables_to_search) == 0:
            tables_to_search = non_empty_table_names

        search_in = {}
        for table_name in tables_to_search:
            search_in[table_name] = self.default_places_to_search[table_name]

        print(keyword)
        print(search_in)

        self.ui.searchTabs = {}
        self.ui.searchTableWidgets = {}

        self.temp_tables_search = {}
        self.temp_stops_search = {}

        self.search_in_list = list(search_in.keys())

        for i, table in enumerate(self.search_in_list):
            # add a tab to ui
            tab = QWidget()
            tab.setObjectName("advancedSearchTab_" + table)
            scrollArea = QScrollArea(tab)
            scrollArea.setGeometry(QtCore.QRect(0, 0, 741, 481))
            scrollArea.setWidgetResizable(True)
            scrollArea.setObjectName("advancedSearchScrollArea_" + table)
            scrollAreaWidgetContents = QWidget()
            scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 739, 479))
            scrollAreaWidgetContents.setObjectName("advancedSearchScrollAreaWidgetContents_" + table)
            mainTableWidget = QTableWidget(scrollAreaWidgetContents)
            mainTableWidget.setGeometry(QtCore.QRect(0, 0, 739, 479))
            mainTableWidget.setObjectName("advancedSearchMainTableWidget_" + table)
            mainTableWidget.setColumnCount(0)
            mainTableWidget.setRowCount(0)
            scrollArea.setWidget(scrollAreaWidgetContents)
            self.ui.searchTabWidget.addTab(tab, "")
            self.ui.searchTabWidget.setTabText(self.ui.searchTabWidget.indexOf(tab), self._translate("MainWindow",  table))
            self.ui.searchTabs[table] = tab
            self.ui.searchTableWidgets[table] = mainTableWidget

            # query
            query = 'SELECT * FROM {} WHERE'.format(table)
            query += ' OR '.join([' ' + col + " LIKE '%" + keyword + "%'" for col in search_in[table]])

            # execute sql query
            c = self.conn.cursor()
            result = c.execute(query)

            self.temp_tables_search[table] = result
            self.temp_stops_search[table] = 0

            col_names = self.get_column_names(table)
            column_count = len(col_names)

            # init table
            self.ui.searchTableWidgets[table].setColumnCount(column_count)
            self.ui.searchTableWidgets[table].setRowCount(0)
            self.ui.searchTableWidgets[table].setHorizontalHeaderLabels(col_names)

            # fill table
            for row_number, row_data in enumerate(result):
                if row_number >= self.MAX_TUPLES_PER_PAGE:
                    self.temp_stops_search[table] = self.MAX_TUPLES_PER_PAGE
                    break

                self.ui.searchTableWidgets[table].insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.searchTableWidgets[table].setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def show_more_search(self):
        active_tab_index = self.ui.searchTabWidget.currentIndex()
        active_tab_table_name = self.search_in_list[active_tab_index]
        active_widget = self.ui.searchTableWidgets[active_tab_table_name]
        # fill table
        for row_number, row_data in enumerate(self.temp_tables_search[active_tab_table_name]):
            if row_number >= self.MAX_TUPLES_PER_PAGE:
                self.temp_stops_search[active_tab_table_name] += self.MAX_TUPLES_PER_PAGE
                break
            active_widget.insertRow(row_number + self.temp_stops_search[active_tab_table_name])
            for column_number, data in enumerate(row_data):
                active_widget.setItem(row_number + self.temp_stops_search[active_tab_table_name], column_number, QTableWidgetItem(str(data)))

    def populate_table_checkboxes(self):
        self.ui.checkBoxes = []
        for i, table_name in enumerate([table for table in self.default_places_to_search if len(self.default_places_to_search[table]) != 0]):
            checkBox = QCheckBox(self.ui.scrollAreaWidgetContents_3)
            checkBox.setGeometry(QtCore.QRect(10, 30 + i*20, 200, 20))
            checkBox.setObjectName("checkBox" + table_name)

            checkBox.setText(self._translate("MainWindow", table_name))
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

            label.setText(self._translate("MainWindow", col))

            self.ui.insertLabels.append(label)

            lineEdit = QLineEdit(self.ui.scrollAreaWidgetContents1)
            lineEdit.setGeometry(QtCore.QRect(170, 10 + i*25, 113, 25))
            lineEdit.setObjectName("insertLineEdit_" + str(i))
            self.ui.insertLineEdits.append(lineEdit)

        # add submit button
        self.ui.submitInsertButton = QPushButton(self.ui.scrollAreaWidgetContents1)
        self.ui.submitInsertButton.setGeometry(QtCore.QRect(20, 10 + 25 * len(col_names), 113, 32))
        self.ui.submitInsertButton.setObjectName("submitInsertButton")
        self.ui.submitInsertButton.setText(self._translate("MainWindow", "Insert"))

        self.ui.submitInsertButton.clicked.connect(self.insert_into_tables)

        # add cancel button
        self.ui.cancelInsertButton = QPushButton(self.ui.scrollAreaWidgetContents1)
        self.ui.cancelInsertButton.setGeometry(QtCore.QRect(150, 10 + 25 * len(col_names), 113, 32))
        self.ui.cancelInsertButton.setObjectName("cancelInsertButton")
        self.ui.cancelInsertButton.setText(self._translate("MainWindow", "Cancel"))

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
        c = self.conn.cursor()
        c.execute(query)
        self.conn.commit()

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

    def finish_delete(self):
        for label in self.ui.deleteLabels:
            label.setParent(None)
        for lineEdit in self.ui.deleteLineEdits:
            lineEdit.setParent(None)
        self.ui.cancelDeleteButton.setParent(None)
        self.ui.submitDeleteButton.setParent(None)
        self.ui.deleteLabels = []
        self.ui.deleteLineEdits = []
        self.ui.scrollAreaWidgetContentsDelete.setParent(None)

    def add_search_details(self):
        # display dialog
        self.advanced_search_dialog = QDialog()
        dialog_win = Ui_Dialog()
        self.dialog_win = dialog_win
        dialog_win.setupUi(self.advanced_search_dialog)
        self.dialog_win.advClearButton.clicked.connect(self.clear_selected_columns)
        self.dialog_win.advDoneButton.clicked.connect(self.close_dialog)

        # fill advTableComboBox
        def table_selected():
            dialog_win.advColumnComboBox.clear()
            dialog_win.advColumnComboBox.clearEditText()
            col_names = self.get_column_names(dialog_win.advTableComboBox.currentText())
            col_names.append('(all)')
            col_names = sorted(col_names)
            dialog_win.advColumnComboBox.addItems(col_names)
            dialog_win.advColumnComboBox.setCurrentIndex(0)
            dialog_win.advColumnComboBox.setCurrentText(col_names[0])
        dialog_win.advTableComboBox.addItems(self.all_table_names)
        dialog_win.advSelectTableButton.clicked.connect(table_selected)

        # bind buttons to actions
        def addPlace():
            table_name = dialog_win.advTableComboBox.currentText()
            col_name = dialog_win.advColumnComboBox.currentText()
            if len(self.places_to_search) == 0 or list(self.places_to_search)[0][0] == table_name:
                if col_name == '(all)':
                    for c in self.get_column_names(table_name):
                        self.add_search_place((table_name, c))
                else:
                    self.add_search_place((table_name, col_name))

                self.updateSelectedColumns()
            else:
                # TODO print error on UI
                print('Cannot do advanced search on two different tables at the same time')

        dialog_win.advAddButton.clicked.connect(addPlace)

        self.advanced_search_dialog.show()
        self.advanced_search_dialog.exec_()

    def add_search_place(self, place):
        self.places_to_search.add(place)

    def updateSelectedColumns(self):
        self.dialog_win.searchPlaces.setColumnCount(2)
        self.dialog_win.searchPlaces.setRowCount(0)
        self.dialog_win.searchPlaces.setHorizontalHeaderLabels(['Table Name', 'Column Name'])

        for i, tup in enumerate(self.places_to_search):
            self.dialog_win.searchPlaces.insertRow(i)
            self.dialog_win.searchPlaces.setItem(i, 0, QTableWidgetItem(str(tup[0])))
            self.dialog_win.searchPlaces.setItem(i, 1, QTableWidgetItem(str(tup[1])))

    def clear_selected_columns(self):
        self.places_to_search = set()
        self.updateSelectedColumns()

    def close_dialog(self):
        self.advanced_search_dialog.close()

    def create_delete_forms(self):
        print('create forms')
        table_name = self.ui.deleteTableComboBox.currentText()
        prim_keys = self.prim_keys[table_name]

        self.ui.scrollAreaWidgetContentsDelete = QWidget()
        self.ui.scrollAreaWidgetContentsDelete.setGeometry(QtCore.QRect(0, 0, 939, 469))
        self.ui.scrollAreaWidgetContentsDelete.setObjectName("scrollAreaWidgetContentsDelete")

        # add labels and forms
        self.ui.deleteLabels = []
        self.ui.deleteLineEdits = []
        for i, prim_key in enumerate(prim_keys):
            label = QLabel(self.ui.scrollAreaWidgetContentsDelete)
            label.setGeometry(QtCore.QRect(10, 10 + i * 25, 131, 20))
            label.setObjectName("deleteLabel_" + str(i))

            label.setText(self._translate("MainWindow", prim_key))

            self.ui.deleteLabels.append(label)

            lineEdit = QLineEdit(self.ui.scrollAreaWidgetContentsDelete)
            lineEdit.setGeometry(QtCore.QRect(170, 10 + i * 25, 113, 25))
            lineEdit.setObjectName("deleteLineEdit_" + str(i))
            self.ui.deleteLineEdits.append(lineEdit)

        # add submit button
        self.ui.submitDeleteButton = QPushButton(self.ui.scrollAreaWidgetContentsDelete)
        self.ui.submitDeleteButton.setGeometry(QtCore.QRect(20, 10 + 25 * len(prim_keys), 113, 32))
        self.ui.submitDeleteButton.setObjectName("submitDeleteButton")
        self.ui.submitDeleteButton.setText(self._translate("MainWindow", "Delete"))

        self.ui.submitDeleteButton.clicked.connect(self.delete_from_table)

        # add cancel button
        self.ui.cancelDeleteButton = QPushButton(self.ui.scrollAreaWidgetContentsDelete)
        self.ui.cancelDeleteButton.setGeometry(QtCore.QRect(150, 10 + 25 * len(prim_keys), 113, 32))
        self.ui.cancelDeleteButton.setObjectName("cancelDeleteButton")
        self.ui.cancelDeleteButton.setText(self._translate("MainWindow", "Cancel"))

        self.ui.cancelDeleteButton.clicked.connect(self.finish_delete)

        # add the whole content to scroll area
        self.ui.scrollArea_tab4.setWidget(self.ui.scrollAreaWidgetContentsDelete)

    def delete_from_table(self):
        table_name = self.ui.deleteTableComboBox.currentText()
        prim_keys = self.prim_keys[table_name]
        values = [lineEdit.text() for lineEdit in self.ui.deleteLineEdits]

        # print('actual delete')
        # prim_key = self.ui.primaryKeyLineEdit.text()

        query = 'DELETE FROM {} WHERE '.format(table_name)
        query += " AND ".join([prim_key + " = '" + val + "'" for prim_key, val in zip(prim_keys, values)])
        print (query)

        # delete
        c = self.conn.cursor()
        c.execute(query)
        self.conn.commit()

        self.finish_delete()

    # functions for predefined queries
    def d1q1(self):
        nbedrooms = self.ui.spinBoxD2Q1.value()
        query = "SELECT AVG(L.price) FROM Listings L WHERE L.bedrooms={}".format(nbedrooms)
        c  = self.conn.cursor()
        c.execute(query)

        price = c.fetchall()[0][0]

        # init table
        self.ui.predefinedMainTableWidget.setColumnCount(1)
        self.ui.predefinedMainTableWidget.setRowCount(0)
        self.ui.predefinedMainTableWidget.setHorizontalHeaderLabels(["Price"])

        # fill table
        self.ui.predefinedMainTableWidget.insertRow(0)
        self.ui.predefinedMainTableWidget.setItem(0, 0, QTableWidgetItem(str(price)))

    def d1q2(self):
        score_field = self.ui.comboBoxD2Q2.currentText()

        query = "SELECT AVG(S.review_scores_{}) " \
                "FROM Has_Scores S, Listings L, Has_Amenities HA, Amenities A " \
                "WHERE A.amenity_name='TV' AND A.amenity_id=HA.amenity_id AND HA.listing_id=L.listing_id AND L.listing_id=S.listing_id"\
            .format(score_field)

        c = self.conn.cursor()
        c.execute(query)
        avg_score = c.fetchall()[0][0]

        # init table
        self.ui.predefinedMainTableWidget.setColumnCount(1)
        self.ui.predefinedMainTableWidget.setRowCount(0)
        self.ui.predefinedMainTableWidget.setHorizontalHeaderLabels(["Score"])

        # fill table
        self.ui.predefinedMainTableWidget.insertRow(0)
        self.ui.predefinedMainTableWidget.setItem(0, 0, QTableWidgetItem(str(avg_score)))

    def d1q3(self):
        start_date = self.all_months_start[self.all_months.index(self.ui.comboBoxD2Q3_start.currentText())]
        start_end = self.all_months_end[self.all_months.index(self.ui.comboBoxD2Q3_end.currentText())]

        query = "SELECT L.HOST_ID, H.HOST_NAME FROM LISTINGS L, HOSTS H WHERE L.HOST_ID = H.HOST_ID " \
                "AND L.LISTING_ID IN " \
                "(SELECT DISTINCT D.LISTING_ID FROM DATES D " \
                "WHERE D.CAL_DATE >= date '{}' AND D.CAL_DATE <= date '{}' " \
                "AND D.AVAILABLE = 't')".format(start_date, start_end)

        print (query)

        c = self.conn.cursor()
        result = c.execute(query)

        # find column headers
        col_names = ["HOST_ID", "HOST_NAME"]

        # init table
        self.ui.predefinedMainTableWidget.setColumnCount(len(col_names))
        self.ui.predefinedMainTableWidget.setRowCount(0)
        self.ui.predefinedMainTableWidget.setHorizontalHeaderLabels(col_names)

        # fill table
        for row_number, row_data in enumerate(result):
            self.ui.predefinedMainTableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.predefinedMainTableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def d1q4(self):
        query = "SELECT COUNT(UNIQUE L.listing_id) FROM Listings L, Hosts H1, Hosts H2 WHERE H1.host_name=H2.host_name AND NOT (H1.host_id=H2.host_id) AND L.host_id=H1.host_id"

        c = self.conn.cursor()
        c.execute(query)
        avg_score = c.fetchall()[0][0]

        # init table
        self.ui.predefinedMainTableWidget.setColumnCount(1)
        self.ui.predefinedMainTableWidget.setRowCount(0)
        self.ui.predefinedMainTableWidget.setHorizontalHeaderLabels(["Number"])

        # fill table
        self.ui.predefinedMainTableWidget.insertRow(0)
        self.ui.predefinedMainTableWidget.setItem(0, 0, QTableWidgetItem(str(avg_score)))

    def d1q5(self):
        query = "SELECT DISTINCT D.cal_date " \
                "FROM Dates D, Listings L, Hosts H " \
                "WHERE H.host_name='Viajes Eco' AND H.host_id=L.host_id AND L.listing_id=D.listing_id AND D.available='t'"

        c = self.conn.cursor()
        result = c.execute(query)

        # find column headers
        col_names = ["Date"]

        # init table
        self.ui.predefinedMainTableWidget.setColumnCount(len(col_names))
        self.ui.predefinedMainTableWidget.setRowCount(0)
        self.ui.predefinedMainTableWidget.setHorizontalHeaderLabels(col_names)

        # fill table
        for row_number, row_data in enumerate(result):
            self.ui.predefinedMainTableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.predefinedMainTableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def d1q6(self):
        nlistings = self.ui.spinBoxD2Q6.value()
        query = "SELECT H.HOST_ID, H.HOST_NAME FROM HOSTS H WHERE {} = ( SELECT COUNT(*) FROM LISTINGS L WHERE L.HOST_ID = H.HOST_ID )".format(nlistings)
        c = self.conn.cursor()
        result = c.execute(query)

        # find column headers
        col_names = ["HOST_ID", "HOST_NAME"]

        # init table
        self.ui.predefinedMainTableWidget.setColumnCount(len(col_names))
        self.ui.predefinedMainTableWidget.setRowCount(0)
        self.ui.predefinedMainTableWidget.setHorizontalHeaderLabels(col_names)

        # fill table
        for row_number, row_data in enumerate(result):
            self.ui.predefinedMainTableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.predefinedMainTableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))


    def d1q7(self):
        amenity_name = self.ui.comboBoxD2Q7.currentText()
        query =  "SELECT avg_wifi - avg_without_wifi " \
                 "FROM ( SELECT AVG(Lw.price) as avg_wifi " \
                 "FROM Listings Lw, Has_Amenities HA, Amenities A " \
                 "WHERE A.amenity_name='{}' AND A.amenity_id=HA.amenity_id AND HA.listing_id=Lw.listing_id) " \
                 "CROSS JOIN (SELECT AVG(L.price) as avg_without_wifi " \
                 "FROM Listings L, Has_Amenities HA, Amenities A " \
                 "WHERE A.amenity_name='{}' AND (HA.amenity_id NOT IN (A.amenity_id)) AND HA.listing_id=L.listing_id)".format(amenity_name, amenity_name)

        c = self.conn.cursor()
        c.execute(query)
        avg_score = c.fetchall()[0][0]

        # init table
        self.ui.predefinedMainTableWidget.setColumnCount(1)
        self.ui.predefinedMainTableWidget.setRowCount(0)
        self.ui.predefinedMainTableWidget.setHorizontalHeaderLabels(["Price"])

        # fill table
        self.ui.predefinedMainTableWidget.insertRow(0)
        self.ui.predefinedMainTableWidget.setItem(0, 0, QTableWidgetItem(str(avg_score)))

    def d1q8(self):
        nbeds = self.ui.spinBoxD2Q8.value()
        query = "SELECT avg_berlin - avg_madrid FROM ( (SELECT AVG (L1.price) AS avg_berlin " \
                "FROM Listings L1, Has_Neighbourhoods N1, Has_Cities C1 " \
                "WHERE L1.beds = {} AND L1.neighbourhood_id = N1.neighbourhood_id AND N1.city_id = C1.city_id AND C1.city = 'Berlin') CROSS JOIN " \
                "(SELECT AVG (L1.price) AS avg_madrid " \
                "FROM Listings L1, Has_Neighbourhoods N1, Has_Cities C1 " \
                "WHERE L1.beds = {} AND L1.neighbourhood_id = N1.neighbourhood_id AND N1.city_id = C1.city_id AND C1.city = 'Madrid') " \
                ")".format(nbeds, nbeds)
        c  = self.conn.cursor()
        c.execute(query)

        price = c.fetchall()[0][0]

        # init table
        self.ui.predefinedMainTableWidget.setColumnCount(1)
        self.ui.predefinedMainTableWidget.setRowCount(0)
        self.ui.predefinedMainTableWidget.setHorizontalHeaderLabels(["Price"])

        # fill table
        self.ui.predefinedMainTableWidget.insertRow(0)
        self.ui.predefinedMainTableWidget.setItem(0, 0, QTableWidgetItem(str(price)))

    def d1q9(self):
        country = self.ui.comboBoxD2Q9.currentText()
        query = "SELECT DISTINCT L1.host_id, H1.host_name " \
                "FROM Listings L1, Hosts H1, Has_Neighbourhoods N1, Has_Cities C1, Countries Cn " \
                "WHERE L1.host_id = H1.host_id AND L1.neighbourhood_id = N1.neighbourhood_id " \
                "AND N1.city_id = C1.city_id AND C1.country_code = Cn.country_code AND Cn.country = '{}' " \
                "Order By (SELECT COUNT (*) FROM Listings L2 WHERE L2.host_id = L1.host_id) DESC FETCH NEXT 10 ROWS ONLY".format(country)

        c = self.conn.cursor()
        result = c.execute(query)

        # find column headers
        col_names = ["HOST_ID", "HOST_NAME"]

        # init table
        self.ui.predefinedMainTableWidget.setColumnCount(len(col_names))
        self.ui.predefinedMainTableWidget.setRowCount(0)
        self.ui.predefinedMainTableWidget.setHorizontalHeaderLabels(col_names)

        # fill table
        for row_number, row_data in enumerate(result):
            self.ui.predefinedMainTableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.predefinedMainTableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def d1q10(self):
        property_type = self.ui.comboBoxD2Q10_pt.currentText()
        city = self.ui.comboBoxD2Q10_c.currentText()
        query = "SELECT L.listing_id, I.LISTING_NAME FROM LISTINGS L " \
                "INNER JOIN (SELECT S.listing_id, S.review_scores_rating from HAS_SCORES S) S " \
                "ON L.listing_id = S.listing_id " \
                "INNER JOIN (SELECT I.listing_id, I.listing_name FROM HAS_INFO I) I " \
                "ON L.listing_id = I.listing_id " \
                "WHERE L.neighbourhood_id in " \
                "(SELECT NEIGHBOURHOOD_ID FROM HAS_NEIGHBOURHOODS WHERE CITY_ID = " \
                "(SELECT CITY_ID FROM HAS_CITIES WHERE CITY = '{}')) " \
                "AND L.property_type_id = " \
                "(SELECT PROPERTY_TYPE_ID FROM PROPERTY_TYPES WHERE PROPERTY_TYPE = '{}') " \
                "ORDER BY S.REVIEW_SCORES_RATING DESC NULLS LAST " \
                "FETCH NEXT 10 ROWS ONLY".format(city, property_type)

        c = self.conn.cursor()
        result = c.execute(query)

        # find column headers
        col_names = ["LISTING_ID", "LISTING_NAME"]

        # init table
        self.ui.predefinedMainTableWidget.setColumnCount(len(col_names))
        self.ui.predefinedMainTableWidget.setRowCount(0)
        self.ui.predefinedMainTableWidget.setHorizontalHeaderLabels(col_names)

        # fill table
        for row_number, row_data in enumerate(result):
            self.ui.predefinedMainTableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.predefinedMainTableWidget.setItem(row_number, column_number,
                                                          QTableWidgetItem(str(data)))

    def close_connection(self):
        self.conn.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())