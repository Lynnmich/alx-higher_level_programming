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

###Use “container-on-demand” to run MySQL
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
