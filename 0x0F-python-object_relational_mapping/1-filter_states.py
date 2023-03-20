#!/usr/bin/python3
"""Write a script that lists all states with a name starting with N (upper N)
        Your script should take 3 arguments: mysql username,
        mysql password and database name (no argument validation needed)
        You must use the module MySQLdb (import MySQLdb)
        Your script should connect to a MySQL server,
        running on localhost at port 3306
        Results must be sorted in ascending order by states.id"""


import MySQLdb
import sys


def filter_states():
    """The filter property to filter the output using MySQLdb"""

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        db = MySQLdb.connect(host="localhost", user=username,
                             password=password, port=3306, database=database)
        """connect() establishes a connection with the UNIX socket"""
        c = db.cursor()
        """cursor() creates a cursor object"""
        c.execute("""SELECT * FROM states WHERE name LIKE "N%"
                    ORDER BY states.id ASC""")
        """execute() executes the query"""
        rows = c.fetchall()
        """fetchall() fetches all the data to be iterated"""
        for row in rows:
            print(row)
        c.close()
        db.close()
    except Exception as e:
        return (e)


if __name__ == "__main__":
    filter_states()
