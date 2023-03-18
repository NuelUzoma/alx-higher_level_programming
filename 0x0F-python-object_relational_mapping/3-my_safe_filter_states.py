#!/usr/bin/python3
"""es, it’s an SQL injection to delete all records of a table…
        Once again, write a script that takes in arguments and
        displays all values in the states table of hbtn_0e_0_usa
        where name matches the argument. But this time,
        write one that is safe from MySQL injections!"""


import MySQLdb
import sys


def my_safe_filter_states():
    """A python function using MySQLdb to test for SQL Injections"""

    USER = sys.argv[1]
    PASSWD = sys.argv[2]
    DATABASE = sys.argv[3]
    STATE_NAME = sys.argv[4]

    try:
        db = MySQLdb.connect(host="localhost", user=USER, password=PASSWD,
                             port=3306, database=DATABASE)
        c = db.cursor()
        c.execute("""SELECT * FROM states WHERE name='%s' OR '1'='1' --
                    ORDER BY states.id ASC""".format(STATE_NAME))
        c.fetchall()
        for row in c:
            print(row)
        db.commit()
        c.close()
        db.close()
    except Exception as e:
        return (e)


if __name__ == "__main__":
    my_safe_filter_states()
