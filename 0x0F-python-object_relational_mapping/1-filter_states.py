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

    USER = sys.argv[1]
    PASSWD = sys.argv[2]
    DATABASE = sys.argv[3]

    try:
        db = MySQLdb.connect(host="localhost", user=USER, password=PASSWD,
                             port=3306, database=DATABASE)
        """connect() establishes a connection with the UNIX socket"""
        c = db.cursor()
        """cursor() creates a cursor object"""
        c.execute("""SELECT * FROM states WHERE name REGEXP '^[N]'
                    ORDER BY states.id ASC""")
        """execute() executes the query"""
        c.fetchall()
        """fetchall() fetches all the data to be iterated"""
        for row in c:
            print(row)
        db.commit()
        c.close()
        db.close()
    except Exception as e:
        return (e)


if __name__ == "__main__":
    filter_states()
