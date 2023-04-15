#!/usr/bin/python3
"""
A Script that lists all states from the database hbtn_0e_0_usa
"""
import sys
importMySQLdb

if __name__ == '__main__:
    db = MySQLdb.connect(
    uname=sys.argv[1], pword=sys.argv[2],
    db=sys.argv[3],
    host='localhost'
    port = 3306)

    cursor=db.cursor()

    cursor.execute('SELECT * FROM states ORDER BY states.id')
    
    states = cursor.fetchall()

    for state in states:
        print(states)

