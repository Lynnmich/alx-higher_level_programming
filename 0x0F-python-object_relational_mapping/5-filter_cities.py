#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
            user=sys.argv[1], passwd=sys.argv[2],
            db=sys.argv[3],
            host='localhost',
            port=3306)
    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
                   INNER JOIN states ON cities.state_id = states.id\
                   WHERE states.name = '%s'\
                   ORDER BY cities.id ASC", (sys.argv[4],))

    cities = cursor.fetchall()
    for row in cities:
        print(" {}: ({})".format(row[0], row[1]))

    cursor.close()
    db.close()
