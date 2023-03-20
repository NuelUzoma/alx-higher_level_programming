#!/usr/bin/python3
"""Write a script that takes in an argument and
        displays all values in the states table of hbtn_0e_0_usa,
        where name matches the argument.
        Your script should take 4 arguments: mysql username, mysql password,
        database name and state name searched (no argument validation needed)
        You must use the module MySQLdb (import MySQLdb)
        Your script should connect to a MySQL server,
        running on localhost at port 3306
        You must use format to create the SQL query with the user input
        Results must be sorted in ascending order by states.id
        Results must be displayed as they are in the example below
        Your code should not be executed when imported"""


import MySQLdb
import sys


def my_filter_states():
    """This function uses the MySQLdb Module to filter states"""

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    STATE_NAME = sys.argv[4]

    try:
        db = MySQLdb.connect(host="localhost", user=username,
                             password=password, port=3306, database=database)
        c = db.cursor()
        c.execute("""SELECT * FROM states WHERE name='{}'
                    ORDER BY states.id ASC""".format(STATE_NAME))
        rows = c.fetchall()
        for row in rows:
            print(row)
        db.commit()
        c.close()
        db.close()
    except Exception as e:
        return (e)


if __name__ == "__main__":
    my_filter_states()
