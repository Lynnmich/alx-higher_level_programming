#!/usr/bin/python3
"""
A script that lists all cities from the database hbtn_0e_4_usa
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

    cursor.execute("SELECT cities.id, cities.name, state.name FROM cities\
                   JOIN states ON cities.state_id=state.id\
                   ORDER BY cities.id ASC")

    cities = cursor.fetchall()

    for city in cities:
        print(city)
