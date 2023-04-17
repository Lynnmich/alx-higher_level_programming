#!/usr/bin/python3
"""
A script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argumet
"""
import sys
import MySQLdb


if __name__ == '__main__':
    """module main function
        Pass name to search for as argument to terminal"""
    uname = sys.argv[1]
    pwd = sys.argv[2]
    dbname = sys.argv[3]
    search = sys.argv[4]
    try:
        db = MySQLdb.connect(host='localhost',
                             user=uname,
                             passwd=pwd,
                             db=dbname, port=3306)
        cur = db.cursor()
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [{}]: {}".format(e.args[0], e.args[1]))
        except IndexError:
            print("MySQL Error: {}".format(e))
        exit(1)

    try:cur.execute("SELECT * FROM states WHERE name like BINARY '{}'\
                     ORDER BY states.id ASC".format(search))
        rows = cur.fetchall()
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [{}]: {}".format(e.args[0], e.args[1]))
        except IndexError:
            print("MySQL Error: {}".format(e))
        cur.close()
        db.close()
        exit(1)

    for item in rows:
        print(item)

    cur.close()
    db.close()

