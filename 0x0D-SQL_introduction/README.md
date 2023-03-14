# MySQL
- Structure Query Language(SQL) is a language used to interact with databases.
A database is a collection of tables.
A table is a collection of related data entries(rows and columns)

- MySQL is a relational database management system(RDBMS).
An RDBMS is a program used to maintain a relational database.

## Requirements
All files were executed on Ubuntu 20.04 LTS using gcc, using python3 (version 3.8.5) and edited using vim.
All files should end with a new line.
All files must be executable.
All SQL queries should have a comment just before.
Al files should start by a comment describing the task.
All SQL keywords should be in uppercase (SELECT, WHERE…).


## Installation

Installing MySQL 8.0 on Ubuntu 20.04 LTS
```
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
```

Connect to your MySQL server:

```
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
```

### Use “container-on-demand” to run MySQL
In the container, credentials are root/root

- Ask for container Ubuntu 20.04
- Connect via SSH
- OR connect via the Web terminal

In the container, you should start MySQL before playing with it:

```
$ service mysql start                                                   
 * Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -p                               
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys                      
$
```

Tasks:

0. Script that lists all databases of your MySQL server. 
1. Script that creates the database hbtn_0c_0 in your MySQL server.
2. Script that deletes the database hbtn_0c_0 in your MySQL server
3. Script that lists all the tables of a database in your MySQL server.
4. Script that creates a table called first_table in the current database in your MySQL server.
5. Script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.
6. Script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.
7. Script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server. 
8. Script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server. 
9. Script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.
10. Script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
11. Script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.
12. Script that updates the score of Bob to 10 in the table second_table. - 12-no_cheating.sql.
13. Script that lists all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.
14. Script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server. 
15. Script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.
16. Script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server. 
17.Script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.
18. Temperatures #0 - Import in hbtn_0c_0 database this table dump: download. Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature. 
19. Temperatures #1 - Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending). 
20. Temperatures #2 - Write a script that displays the max temperature of each state (ordered by State name).
