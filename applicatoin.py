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
    all_cities = ['Barcelona', 'Berlin', 'Madrid']
    all_property_types = ['Apartment']
    all_room_types = ['Private Room']
    all_review_score_types = ['review_scores_rating', 'review_scores_accuracy', 'review_scores_cleanliness',
                                       'review_scores_checkin', 'review_scores_communication', 'review_scores_location',
                                       'review_scores_value']
    all_months_start = ['2018-11-07', '2018-12-01', '2019-01-01', '2019-02-01', '2019-03-01', '2019-04-01', '2019-05-01', '2019-06-01', '2019-07-01', '2019-08-01', '2019-09-01', '2019-10-01', '2019-11-01']
    all_months_end = ['2018-11-30', '2018-12-31', '2019-01-31', '2019-02-28', '2019-03-31', '2019-04-30', '2019-05-31', '2019-06-30', '2019-07-31', '2019-08-31', '2019-09-30', '2019-10-31', '2019-11-30']
    all_months = ['2018-11', '2018-12', '2019-01', '2019-02', '2019-03', '2019-04', '2019-05', '2019-06', '2019-07', '2019-08', '2019-09', '2019-10', '2019-11']
    default_places_to_search = {'AMENITIES': ['AMENITY_NAME'],
                                'BED_TYPES': ['BED_TYPE'],
                                'CANCELLATION_POLICIES': ['CANCELLATION_POLICY'],
                                'COUNTRIES': ['COUNTRY'],
                                'DATES': ['CAL_DATE'],
                                'HAS_AMENITIES': ['AMENITY_ID'],
                                'HAS_CITIES': ['CITY'],
                                'HAS_INFO': ['LISTING_NAME', 'SUMMARY_INFO', 'SPACE_INFO', 'NEIGHBORHOOD_OVERVIEW'],
                                'HAS_NEIGHBOURHOODS': ['NEIGHBOURHOOD'],
                                'HAS_SCORES': [],
                                'HAS_VERIFICATIONS': [],
                                'HOST_RESPONSE_TIMES': [],
                                'HOSTS': ['HOST_NAME'],
                                'LISTINGS': [],
                                'PRICES': [],
                                'PROPERTY_TYPES': ['PROPERTY_TYPE'],
                                'REVIEWED_BY': [],
                                'ROOM_TYPES': [],
                                'RULES': [],
                                'UI_TEST': [],
                                'VERIFICATIONS': ['VERIFICATION']
                                }

    def __init__(self):
        dsn_tns = cx_Oracle.makedsn('cs322-db.epfl.ch', '1521', sid='ORCLCDB')
        self.conn = cx_Oracle.connect(user=r'C##DB2019_G48', password='DB2019_G48', dsn=dsn_tns)
        c = self.conn.cursor()

        self.get_table_names()
        self.get_primary_keys()
        self.get_all_amenities()
        self.get_all_property_types()
        self.get_all_room_types()


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
        self.ui.comboBoxD2Q10_c.addItems(self.all_cities)
        self.ui.comboBoxD2Q10_c.setCurrentText('Barcelona')
        self.ui.comboBoxD2Q10_pt.addItems(self.all_property_types)
        self.ui.comboBoxD2Q10_pt.setCurrentText('Apartment')


        self.ui.comboBoxD3Q2_review.addItems(self.all_review_score_types)
        self.ui.comboBoxD3Q2_review.setCurrentText('review_scores_rating')
        self.ui.comboBoxD3Q2_city.addItems(self.all_cities)
        self.ui.comboBoxD3Q2_city.setCurrentText('Madrid')
        self.ui.comboBoxD3Q4_city.addItems(self.all_cities)
        self.ui.comboBoxD3Q4_city.setCurrentText('Berlin')
        self.ui.comboBoxD3Q4_start.addItems(self.all_months_start)
        self.ui.comboBoxD3Q4_start.setCurrentText('2019-03-01')
        self.ui.comboBoxD3Q4_end.addItems(self.all_months_end)
        self.ui.comboBoxD3Q4_end.setCurrentText('2019-04-30')
        self.ui.spinBoxD3Q4_beds.setValue(2)
        self.ui.spinBoxD3Q4_score.setValue(8)
        self.ui.spinBoxD3Q4_score.setMaximum(10)

        self.ui.comboBoxD3Q5.addItems(self.all_review_score_types)
        self.ui.comboBoxD3Q5.setCurrentText('review_scores_rating')
        self.ui.comboBoxD3Q7_city.addItems(self.all_cities)
        self.ui.comboBoxD3Q7_city.setCurrentText('Berlin')
        self.ui.comboBoxD3Q7_room_type.addItems(self.all_room_types)
        self.ui.comboBoxD3Q7_room_type.setCurrentText('Private room')
        self.ui.comboBoxD3Q8.addItems(self.all_review_score_types)
        self.ui.comboBoxD3Q8.setCurrentText('review_scores_communication')
        self.ui.spinBoxD3Q9.setValue(3)
        self.ui.comboBoxD3Q10_city.addItems(self.all_cities)
        self.ui.comboBoxD3Q10_city.setCurrentText('Madrid')
        self.ui.spinBoxD3Q10.setValue(50)
        self.ui.spinBoxD3Q10.setMaximum(100)
        self.ui.spinBoxD3Q11.setValue(20)
        self.ui.spinBoxD3Q11.setMaximum(100)
        self.ui.comboBoxD3Q12.addItems(self.all_cities)
        self.ui.comboBoxD3Q12.setCurrentText('Barcelona')
        self.ui.spinBoxD3Q12.setValue(5)
        self.ui.spinBoxD3Q12.setMaximum(100)

        # predefined query functions
        self.ui.predefinedQueryButtonD2Q1.clicked.connect(self.d2q1)
        self.ui.predefinedQueryButtonD2Q2.clicked.connect(self.d2q2)
        self.ui.predefinedQueryButtonD2Q3.clicked.connect(self.d2q3)
        self.ui.predefinedQueryButtonD2Q4.clicked.connect(self.d2q4)
        self.ui.predefinedQueryButtonD2Q5.clicked.connect(self.d2q5)
        self.ui.predefinedQueryButtonD2Q6.clicked.connect(self.d2q6)
        self.ui.predefinedQueryButtonD2Q7.clicked.connect(self.d2q7)
        self.ui.predefinedQueryButtonD2Q8.clicked.connect(self.d2q8)
        self.ui.predefinedQueryButtonD2Q9.clicked.connect(self.d2q9)
        self.ui.predefinedQueryButtonD2Q10.clicked.connect(self.d2q10)

        self.ui.predefinedQueryButtonD3Q1.clicked.connect(self.d3q1)
        self.ui.predefinedQueryButtonD3Q2.clicked.connect(self.d3q2)
        self.ui.predefinedQueryButtonD3Q3.clicked.connect(self.d3q3)
        self.ui.predefinedQueryButtonD3Q4.clicked.connect(self.d3q4)
        self.ui.predefinedQueryButtonD3Q5.clicked.connect(self.d3q5)
        self.ui.predefinedQueryButtonD3Q6.clicked.connect(self.d3q6)
        self.ui.predefinedQueryButtonD3Q7.clicked.connect(self.d3q7)
        self.ui.predefinedQueryButtonD3Q8.clicked.connect(self.d3q8)
        self.ui.predefinedQueryButtonD3Q9.clicked.connect(self.d3q9)
        self.ui.predefinedQueryButtonD3Q10.clicked.connect(self.d3q10)
        self.ui.predefinedQueryButtonD3Q11.clicked.connect(self.d3q11)
        self.ui.predefinedQueryButtonD3Q12.clicked.connect(self.d3q12)

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

    def get_all_room_types(self):
        c = self.conn.cursor()
        c.execute("Select ROOM_TYPE from ROOM_TYPES")
        self.all_room_types = [x[0] for x in c.fetchall()]

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
    def d2q1(self):
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

    def d2q2(self):
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

    def d2q3(self):
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

    def d2q4(self):
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

    def d2q5(self):
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

    def d2q6(self):
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


    def d2q7(self):
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

    def d2q8(self):
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

    def d2q9(self):
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

    def d2q10(self):
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

    def print_result_predefined_3(self, query, col_names):
        c = self.conn.cursor()
        result = c.execute(query)

        # find column headers
        # col_names = ["HOST_ID", "HOST_NAME"]

        # init table
        self.ui.predefined3MainTableWidget.setColumnCount(len(col_names))
        self.ui.predefined3MainTableWidget.setRowCount(0)
        self.ui.predefined3MainTableWidget.setHorizontalHeaderLabels(col_names)

        # fill table
        for row_number, row_data in enumerate(result):
            self.ui.predefined3MainTableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.predefined3MainTableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def d3q1(self):
        query = "WITH Hosts_city AS (" \
                "SELECT L.host_id, HC.city " \
                "FROM Listings L, Has_Neighbourhoods HN, Has_Cities HC " \
                "WHERE L.square_feet IS NOT NULL AND L.neighbourhood_id=HN.neighbourhood_id AND HN.city_id=HC.city_id " \
                ") " \
                "SELECT COUNT(*) AS n_hosts, HOC.city " \
                "FROM Hosts_city HOC " \
                "GROUP BY HOC.city " \
                "ORDER BY HOC.city"

        self.print_result_predefined_3(query, ["N_HOSTS", "CITY"])

    def d3q2(self):
        score_field = self.ui.comboBoxD3Q2_review.currentText()
        city = self.ui.comboBoxD3Q2_city.currentText()

        query = "WITH Listings_neigh_scores AS (" \
                "    SELECT L.listing_id, L.neighbourhood_id, HS.{}" \
                "    FROM Listings L, Has_Scores HS, Has_Neighbourhoods HN1, Has_Cities HC" \
                "    WHERE L.listing_id=HS.listing_id AND L.neighbourhood_id=HN1.neighbourhood_id AND HN1.city_id=HC.city_id AND HC.city='{}' AND HS.{} IS NOT NULL" \
                "), Neigh_median AS (" \
                "    SELECT" \
                "       neighbourhood_id," \
                "       AVG({}) AS median_score" \
                "    FROM" \
                "    (" \
                "       SELECT" \
                "          neighbourhood_id," \
                "          {}," \
                "          ROW_NUMBER() OVER (" \
                "         PARTITION BY neighbourhood_id" \
                "         ORDER BY {} ASC) AS row_asc," \
                "          ROW_NUMBER() OVER (" \
                "         PARTITION BY neighbourhood_id" \
                "         ORDER BY {} DESC) AS row_desc" \
                "       FROM Listings_neigh_scores" \
                "    )" \
                "    WHERE" \
                "       row_asc IN (row_desc, row_desc - 1, row_desc + 1)" \
                "    GROUP BY neighbourhood_id" \
                "    ORDER BY neighbourhood_id" \
                ")" \
                " SELECT HN.neighbourhood" \
                " FROM Neigh_median NM, Has_Neighbourhoods HN" \
                " WHERE NM.neighbourhood_id=HN.neighbourhood_id" \
                " ORDER BY NM.median_score DESC" \
                " FETCH NEXT 5 ROWS ONLY".format(score_field, city, score_field, score_field, score_field, score_field, score_field)

        print(query)
        self.print_result_predefined_3(query, ['NEIGHBOURHOOD'])

    def d3q3(self):
        query = "SELECT H.HOST_ID, H.HOST_NAME FROM HOSTS H " \
                "WHERE H.HOST_ID = ( " \
                "SELECT L.HOST_ID FROM LISTINGS L " \
                "GROUP BY L.HOST_ID " \
                "ORDER BY COUNT(*) DESC " \
                "FETCH NEXT ROW ONLY)"

        self.print_result_predefined_3(query, ["HOST_ID", "HOST_NAME"])

    def d3q4(self):
        start = self.ui.comboBoxD3Q4_start.currentText()
        end = self.ui.comboBoxD3Q4_end.currentText()
        city = self.ui.comboBoxD3Q4_city.currentText()
        beds = self.ui.spinBoxD3Q4_beds.value()
        rating = self.ui.spinBoxD3Q4_score.value()

        query = "SELECT D.listing_id, AVG(D.price) AS avg_prices " \
                "FROM Dates D, Listings L, Has_Neighbourhoods HN, Has_Cities HC, Has_Scores HS, Property_Types PT, Rules R, Cancellation_Policies CP, Has_Verifications HV, Verifications V " \
                "WHERE L.beds>{} " \
                "    AND L.neighbourhood_id=HN.neighbourhood_id AND HN.city_id=HC.city_id AND HC.city='{}' " \
                "    AND L.listing_id=HS.listing_id AND HS.review_scores_location>={} " \
                "    AND L.property_type_id=PT.property_type_id AND PT.property_type='Apartment' " \
                "    AND L.listing_id=R.listing_id AND R.cancellation_policy_id=CP.cancellation_policy_id AND CP.cancellation_policy='flexible' " \
                "    AND L.listing_id=D.listing_id AND D.cal_date>=to_date('{}', 'YYYY-MM-DD') AND D.cal_date<=to_date('{}', 'YYYY-MM-DD') AND D.available='t' " \
                "    AND L.host_id=HV.host_id AND HV.verification_id=V.verification_id AND V.verification='government_id' " \
                "GROUP BY D.listing_id " \
                "ORDER BY avg_prices ASC " \
                "FETCH NEXT 5 ROWS ONLY".format(beds-1, city, rating, start, end)

        self.print_result_predefined_3(query, ['LISTING_ID', 'AVG_PRICES'])

    def d3q5(self):
        score_field = self.ui.comboBoxD3Q5.currentText()
        print(score_field)
        query = "SELECT * FROM" \
                "(" \
                "  WITH LISTING_RATINGS AS" \
                "  (" \
                "    SELECT L.LISTING_ID, L.ACCOMMODATES, S.{} FROM LISTINGS L" \
                "    INNER JOIN HAS_SCORES S ON L.LISTING_ID = S.LISTING_ID" \
                "    WHERE L.LISTING_ID IN" \
                "    (" \
                "      SELECT HA.LISTING_ID FROM HAS_AMENITIES HA" \
                "      WHERE HA.AMENITY_ID IN" \
                "      (" \
                "        SELECT AMENITY_ID FROM AMENITIES" \
                "        WHERE AMENITY_NAME IN ('Wifi', 'Internet', 'TV', 'Free street parking')" \
                "      )" \
                "      GROUP BY HA.LISTING_ID" \
                "      HAVING COUNT(HA.AMENITY_ID) >= 2" \
                "    )" \
                "  )" \
                "  SELECT LR.ACCOMMODATES, LR.LISTING_ID, RANK() OVER" \
                "  (" \
                "    PARTITION BY LR.ACCOMMODATES" \
                "    ORDER BY LR.{} DESC NULLS LAST" \
                "  ) HIGHEST_RATED" \
                "  FROM LISTING_RATINGS LR" \
                ")" \
                "WHERE HIGHEST_RATED <= 5"\
            .format(score_field, score_field)

        self.print_result_predefined_3(query, ['ACCOMODATES', 'LISTING_ID', 'HIGEST_RATED'])

    def d3q6(self):
        query = "SELECT * FROM " \
                "( " \
                "  WITH BUSYNESS AS ( " \
                "    SELECT L.HOST_ID, L.LISTING_ID, COUNT(R.REVIEW_ID) NUM_REVIEWS FROM LISTINGS L " \
                "    INNER JOIN REVIEWED_BY R ON L.LISTING_ID = R.LISTING_ID " \
                "    GROUP BY L.HOST_ID, L.LISTING_ID " \
                "  ) " \
                "  SELECT B.HOST_ID, B.LISTING_ID, RANK() OVER " \
                "  ( " \
                "    PARTITION BY B.HOST_ID " \
                "    ORDER BY B.NUM_REVIEWS DESC " \
                "  ) AS BUSYNESS_RANK " \
                "  FROM BUSYNESS B " \
                ")  " \
                "WHERE BUSYNESS_RANK <= 3"

        self.print_result_predefined_3(query, ['HOST_ID', 'LISTING_ID', 'BUSYNESS_RANK'])

    def d3q7(self):
        room_type = self.ui.comboBoxD3Q7_room_type.currentText()
        city = self.ui.comboBoxD3Q7_city.currentText()

        query = "SELECT * FROM " \
                "( " \
                "  WITH AMENITY_USES AS " \
                "  ( " \
                "    SELECT L.NEIGHBOURHOOD_ID, A.AMENITY_ID, COUNT(L.LISTING_ID) NUM_LISTINGS " \
                "    FROM LISTINGS L " \
                "    INNER JOIN HAS_NEIGHBOURHOODS N ON L.NEIGHBOURHOOD_ID = N.NEIGHBOURHOOD_ID " \
                "    INNER JOIN HAS_CITIES C ON N.CITY_ID = C.CITY_ID " \
                "    INNER JOIN HAS_AMENITIES A ON L.LISTING_ID = A.LISTING_ID " \
                "    WHERE L.ROOM_TYPE_ID = ( " \
                "      SELECT R.ROOM_TYPE_ID FROM ROOM_TYPES R " \
                "      WHERE R.ROOM_TYPE = '{}' " \
                "    ) " \
                "    AND C.CITY = '{}' " \
                "    GROUP BY L.NEIGHBOURHOOD_ID, A.AMENITY_ID " \
                "  ) " \
                "  SELECT AU.NEIGHBOURHOOD_ID, AU.AMENITY_ID, RANK() OVER " \
                "  ( " \
                "    PARTITION BY NEIGHBOURHOOD_ID " \
                "    ORDER BY NUM_LISTINGS DESC " \
                "  ) MOST_USED " \
                "  FROM AMENITY_USES AU " \
                ") " \
                "WHERE MOST_USED <= 3".format(room_type, city)

        self.print_result_predefined_3(query, ['NEIGHBOURHOOD_ID', 'AMENITY_ID', 'MOST_USED'])

    def d3q8(self):
        score_field = self.ui.comboBoxD3Q8.currentText()

        query = "WITH Host_nVerifications AS ( " \
                "    SELECT DISTINCT H.host_id, 0 AS n_verifications " \
                "    FROM Hosts H " \
                "    WHERE H.host_id NOT IN ( " \
                "        SELECT HV.host_id " \
                "        FROM Has_Verifications HV) " \
                "    UNION " \
                "    SELECT HV.host_id, COUNT(*) as n_verifications " \
                "    FROM Has_Verifications HV " \
                "    GROUP BY HV.host_id " \
                "), " \
                "Host_nVerifications_rscommunication AS ( " \
                "    SELECT HNV.*, HS.{} " \
                "    FROM Host_nVerifications HNV, Listings L, Has_Scores HS " \
                "    WHERE HNV.host_id=L.host_id AND L.listing_id=HS.listing_id AND HS.{} IS NOT NULL " \
                ") " \
                "SELECT review_scores_communication_highest - review_scores_communication_lowest " \
                "FROM ( " \
                "    SELECT HNVR.{} AS review_scores_communication_highest " \
                "    FROM Host_nVerifications_rscommunication HNVR " \
                "    ORDER BY HNVR.n_verifications DESC " \
                "    FETCH NEXT 1 ROWS ONLY) " \
                "CROSS JOIN ( " \
                "    SELECT HNVR.{} AS review_scores_communication_lowest " \
                "    FROM Host_nVerifications_rscommunication HNVR " \
                "    ORDER BY HNVR.n_verifications ASC " \
                "    FETCH NEXT 1 ROWS ONLY)".format(score_field, score_field, score_field, score_field)

        self.print_result_predefined_3(query, ['REVIEW_SCORE_DIFFERENCE'])

    def d3q9(self):
        n_acc = self.ui.spinBoxD3Q9.value()

        query = "SELECT C.CITY FROM LISTINGS L " \
                "INNER JOIN HAS_NEIGHBOURHOODS N ON L.NEIGHBOURHOOD_ID = N.NEIGHBOURHOOD_ID " \
                "INNER JOIN HAS_CITIES C ON N.CITY_ID = C.CITY_ID " \
                "INNER JOIN REVIEWED_BY R ON L.LISTING_ID = R.LISTING_ID " \
                "WHERE L.ROOM_TYPE_ID IN " \
                "  (SELECT ROOM_TYPE_ID FROM LISTINGS " \
                "  GROUP BY ROOM_TYPE_ID " \
                "  HAVING AVG(ACCOMMODATES) > {}) " \
                "GROUP BY C.CITY " \
                "ORDER BY COUNT(L.LISTING_ID) DESC " \
                "FETCH NEXT ROW ONLY".format(n_acc)

        self.print_result_predefined_3(query, ['CITY'])

    def d3q10(self):
        city = self.ui.comboBoxD3Q10_city.currentText()
        perc = self.ui.spinBoxD3Q10.value()

        query = "WITH Listings_filtered AS ( " \
                "    SELECT L.listing_id, L.neighbourhood_id " \
                "    FROM Listings L, Has_Neighbourhoods HN, Has_Cities HC, Hosts H " \
                "    WHERE L.neighbourhood_id=HN.neighbourhood_id AND HN.city_id=HC.city_id AND HC.city='{}' AND L.host_id=H.host_id AND H.host_since<=to_date('2017-06-01', 'YYYY-MM-DD') " \
                "), Neigh_ndl AS ( " \
                "    SELECT COUNT(*) * (to_date('2020-01-01', 'YYYY-MM-DD') - to_date('2019-01-01', 'YYYY-MM-DD')) AS n_days_listings, LF.neighbourhood_id " \
                "    FROM Listings_filtered LF " \
                "    GROUP BY LF.neighbourhood_id " \
                "), Neigh_ndl_a AS ( " \
                "    SELECT COUNT(*) AS n_days_listings_available, LF.neighbourhood_id " \
                "    FROM Listings_filtered LF, Dates D " \
                "    WHERE D.cal_date>=to_date('2019-01-01', 'YYYY-MM-DD') AND D.cal_date<to_date('2020-01-01', 'YYYY-MM-DD') AND LF.listing_id=D.listing_id AND D.available='t' " \
                "    GROUP BY LF.neighbourhood_id " \
                ") " \
                "SELECT HN.neighbourhood " \
                "FROM Neigh_ndl NDL, Neigh_ndl_a NDLA, Has_Neighbourhoods HN " \
                "WHERE NDL.neighbourhood_id=NDLA.neighbourhood_id AND NDLA.n_days_listings_available/NDL.n_days_listings>={} AND HN.neighbourhood_id=NDL.neighbourhood_id".format(city, str(int(perc)/100))

        self.print_result_predefined_3(query, ['NEIGHBOURHOOD'])

    def d3q11(self):
        perc = self.ui.spinBoxD3Q11.value()

        query = "WITH LISTING_COUNTRIES AS " \
                "( " \
                "  SELECT LISTING_ID, C.COUNTRY FROM LISTINGS L " \
                "  INNER JOIN HAS_NEIGHBOURHOODS N ON L.NEIGHBOURHOOD_ID = N.NEIGHBOURHOOD_ID " \
                "  INNER JOIN HAS_CITIES HC ON N.CITY_ID = HC.CITY_ID " \
                "  INNER JOIN COUNTRIES C ON HC.COUNTRY_CODE = C.COUNTRY_CODE " \
                "), NUM_LISTINGS AS " \
                "( " \
                "  SELECT COUNTRY, COUNT(LISTING_ID) TOTAL FROM LISTING_COUNTRIES " \
                "  GROUP BY COUNTRY " \
                "), AVAILABLE_IN_2018 AS " \
                "( " \
                "  SELECT L.COUNTRY, COUNT(DISTINCT L.LISTING_ID) AVAILABLE FROM DATES D " \
                "  INNER JOIN LISTING_COUNTRIES L ON D.LISTING_ID = L.LISTING_ID " \
                "  WHERE D.AVAILABLE = 't' " \
                "  AND D.CAL_DATE >= to_date('2018-01-01', 'YYYY-MM-DD') AND D.CAL_DATE <= to_date('2018-12-31', 'YYYY-MM-DD') " \
                "  GROUP BY L.COUNTRY " \
                ") " \
                "SELECT N.COUNTRY FROM NUM_LISTINGS N " \
                "INNER JOIN AVAILABLE_IN_2018 A ON N.COUNTRY = A.COUNTRY " \
                "WHERE A.AVAILABLE >= N.TOTAL / {}".format(str(100/int(perc)))

        self.print_result_predefined_3(query, ['COUNTRY'])

    def d3q12(self):
        city = self.ui.comboBoxD3Q12.currentText()
        perc = self.ui.spinBoxD3Q12.value()

        query = "WITH L_{}_cancellation AS ( " \
                "    SELECT L.listing_id, L.neighbourhood_id, CP.cancellation_policy " \
                "    FROM Listings L, Rules R, Cancellation_Policies CP, Has_Neighbourhoods HN, Has_Cities HC " \
                "    WHERE L.listing_id=R.listing_id AND R.cancellation_policy_id=CP.cancellation_policy_id AND L.neighbourhood_id=HN.neighbourhood_id AND HN.city_id=HC.city_id AND HC.city='{}' " \
                "), Neigh_n_listings_strict AS ( " \
                "    SELECT COUNT(*) AS n_listings_strict, LBC.neighbourhood_id " \
                "    FROM L_{}_cancellation LBC " \
                "    WHERE LBC.cancellation_policy='strict_14_with_grace_period' " \
                "    GROUP BY LBC.neighbourhood_id " \
                "), Neigh_n_listings AS ( " \
                "    SELECT COUNT(*) AS n_listings, LBC.neighbourhood_id " \
                "    FROM L_{}_cancellation LBC " \
                "    GROUP BY LBC.neighbourhood_id " \
                "), Neigh_percent_strict AS ( " \
                "    SELECT NLS.neighbourhood_id, NLS.n_listings_strict * 100 / NL.n_listings AS percent_strict " \
                "    FROM Neigh_n_listings_strict NLS, Neigh_n_listings NL " \
                "    WHERE NLS.neighbourhood_id=NL.neighbourhood_id " \
                ") " \
                "SELECT HN.neighbourhood " \
                "FROM Neigh_percent_strict NPS, Has_Neighbourhoods HN " \
                "WHERE NPS.percent_strict>={} AND NPS.neighbourhood_id=HN.neighbourhood_id".format(city, city, city, city, perc)

        self.print_result_predefined_3(query, ['NEIGHBOURHOOD'])

    def close_connection(self):
        self.conn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())