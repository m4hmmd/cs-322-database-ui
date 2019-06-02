# cs-322-database-ui
A minimalistic user interface to communicate with an Oracle database, in this case designed to make queries and get insights about Airbnb data that we have cleaned and uploaded to the server.

The program accommodates basic functionalities such as insert, delete, search for keywords, print the tables and run predefined queries from the two milestones of the Intoduction to Database Systems course at EPFL. The queries can be parametrized in most cases, with the use of drop down menus. 

The printing of results is done in a tabular way, just like in SQLDeveloper or other SQL programs. Also similar to those, since some outputs are prohibitively long, buffering is used when printing the results: at most 1000 rows are printed for any user request, and the next 1000 can be accessed using the provided ‘more’ button. 

The different functionalities in the interface are collected into different tabs, which are: Print Tables, Search, Advanced Search, Insert, Delete, Predefined 2, Predefined 3. The last two accommodate the predefined queries from the deliverables 2 and 3, respectively. 

The technologies we used in development are:  

* cx_Oracle library for interacting with the database 
* PyQt5 for interface elements and bindings 
* Qt Designer for easy manipulation of PyQt5 elements in a drag-and-drop manner 

## Screenshots 

##### Print Tables: Select a table present in the database and print its entire content.  

![alt text](https://github.com/m4hmmd/cs-322-database-ui/blob/master/screenshots/print_tables.png)

##### Search: Search for a keyword match in either the entire db, or selected tables. The search is performed on preselected columns for each table, which in our opinion are the columns in which it makes sense to search for a keyword. 

![alt text](https://github.com/m4hmmd/cs-322-database-ui/blob/master/screenshots/search.png)

##### Advanced Search: Search for a keyword match in selected columns of a selected table. The user presses ‘Advanced’ button, then selects the table and columns, and adds them to the list of places to be searched. 

![alt text](https://github.com/m4hmmd/cs-322-database-ui/blob/master/screenshots/adv_search.png)

##### Insert: Select a table, get a form with the column names of the table and insert a row by filling the from. 

![alt text](https://github.com/m4hmmd/cs-322-database-ui/blob/master/screenshots/insert.png)

##### Delete: Select a table, get a form with the column names of its primary key, and delete by specifying pk. 

![alt text](https://github.com/m4hmmd/cs-322-database-ui/blob/master/screenshots/delete.png)

##### Predefined 2 & 3: Run the predefined queries, possibly with different parameters of your choice. 

![alt text](https://github.com/m4hmmd/cs-322-database-ui/blob/master/screenshots/d2q10.png)
![alt text](https://github.com/m4hmmd/cs-322-database-ui/blob/master/screenshots/d3q4.png)


 
