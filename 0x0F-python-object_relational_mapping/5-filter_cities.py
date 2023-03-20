#!/usr/bin/python3
"""Write a script that takes in the name of a state as an argument and
        lists all cities of that state, using the database hbtn_0e_4_usa
        Your script should take 4 arguments:
        mysql username, mysql password, database name and
        state name (SQL injection free!)
        You must use the module MySQLdb (import MySQLdb)
        Your script should connect to a MySQL server
        running on localhost at port 3306
        Results must be sorted in ascending order by cities.id
        You can use only execute() once"""


import MySQLdb
import sys


def filter_cities():
    """The python function using Mysqldb module to filter cities"""

    USER = sys.argv[1]
    PASSWD = sys.argv[2]
    DATABASE = sys.argv[3]
    STATE_NAME = sys.argv[4]

    try:
        db = MySQLdb.connect(host="localhost", user=USER, password=PASSWD,
                             port=3306, database=DATABASE)
        c = db.cursor()
        c.execute("""SELECT name FROM cities
                    WHERE state_id= (
                        SELECT id
                        FROM states
                        WHERE name = %s
                        )
                        """, (STATE_NAME, ))
        cities = c.fetchall()
        my_string = ""
        for i in range(len(cities)):
            (city,) = cities[i]
            if i != len(cities) - 1:
                my_string = my_string + "{}, ".format(city)
            else:
                my_string = my_string + city
        print(my_string)
        db.commit()
        c.close()
        db.close()
    except Exception as e:
        return (e)


if __name__ == "__main__":
    filter_cities()
