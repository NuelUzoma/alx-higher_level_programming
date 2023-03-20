#!/usr/bin/python3
"""Write a script that lists all cities from the database hbtn_0e_4_usa
        Your script should take 3 arguments: mysql username,
        mysql password and database name
        You must use the module MySQLdb (import MySQLdb)
        Your script should connect to a MySQL server
        unning on localhost at port 3306
        Results must be sorted in ascending order by cities.id
        You can use only execute() once"""


import MySQLdb
import sys


def cities_by_states():
    """A Python Function using the MySQLdb Module to list cities by states"""

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        db = MySQLdb.connect(host="localhost", user=username,
                             password=password, port=3306, database=database)
        c = db.cursor()
        c.execute("""SELECT cities.id, cities.name, states.name FROM cities
                    JOIN states ON cities.state_id = states.id
                    ORDER BY cities.id ASC""")
        rows = c.fetchall()
        for row in rows:
            print(row)
        db.commit()
        c.close()
        db.close()
    except Exception as e:
        return (e)


if __name__ == "__main__":
    cities_by_states()
