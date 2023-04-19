#!/usr/bin/python3
"""
A script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument
"""
import sys
import MySQLdb


if __name__ == '__main__':

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'ORDER BY\
                   states.id ASC".format(sys.argv[4]))

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
