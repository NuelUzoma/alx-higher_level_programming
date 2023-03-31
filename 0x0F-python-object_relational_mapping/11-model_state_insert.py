#!/usr/bin/python3
"""
Write a Script that adds the State Object Louisiana to the database hbtn_0e_usa
Your script should take 3 arguments: mysql username,
mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state -
from model_state import Base, State
Your script should connect to a MySQL server running on localhost at port 3306
Print the new states.id after creation
Your code should not be executed when imported"""


if __name__ == "__main__":
    from model_state import Base, State
    import sys
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    USER = sys.argv[1]
    PWD = sys.argv[2]
    DB = sys.argv[3]

    engine = create_engine('m')