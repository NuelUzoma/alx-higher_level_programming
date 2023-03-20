#!/usr/bin/python3
"""Write a python file that contains the class definition of a State
and an instance Base = declarative_base():
State class:
inherits from Base Tips
links to the MySQL table states
class attribute id that represents a column of an auto-generated,
unique integer, cannot be null and is a primary key
class attribute name that represents a column of a string
with maximum 128 characters and cannot be null
WARNING: all classes who inherit from Base must be imported
before calling Base.metadata.create_all(engine)
"""


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy import Column, String, Integer
    from sqlalchemy.ext.declarative import declarative_base
    import sys

    USR = sys.argv[1]
    PWD = sys.argv[2]
    DB = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(USR, PWD, DB), pool_pre_ping=True)
    Base = declarative_base()

    class State(Base):
        """State Class that inherits from base linking to the states table"""
        __tablename__ = 'states'

        id = Column(Integer, primary_key=True,
                    autoincrement=True, nullable=False)
        name = Column(String(128), nullable=False)

        def __init__(self, id, name):
            """The initialization of the State class using SQLAlchemy"""
            self.id = id
            self.name = name

    Base.metadata.create_all(engine)
