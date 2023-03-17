#!/usr/bin/python3
"""Write a script that lists all states from the database
        hbtn_0e_0_usa Your script should take 3 arguments:
        mysql username, mysql password and database name
        (no argument validation needed)
        You must use the module MySQLdb (import MySQLdb)
        Your script should connect to a MySQL server,
        running on localhost at port 3306
        Results must be sorted in ascending order by states.id"""


import MySQLdb
import sys


def select_states():
    """The SQL Python Script to query all states"""

    USER = sys.argv[1]
    PASSWD = sys.argv[2]
    DATABASE = sys.argv[3]

    try:
        db = MySQLdb.connect(host="localhost", user=USER, password=PASSWD,
                             port=3306, database=DATABASE)
        """The connect function establehes a connection with the UNIX socket"""
        c = db.cursor()
        """The cursor function creates a cursor object using cursor()"""
        c.execute("""SELECT * FROM states ORDER BY states.id ASC""")
        """The execute function executes the SQL Query using exeute()"""
        c.fetchall()
        """The fetchall() fetches all the rows and columns in the table"""
        for row in c:
            print(row)
        db.commit()
        c.close()
        db.close()
    except Exception as e:
        return (e)


if __name__ == "__main__":
    select_states()
