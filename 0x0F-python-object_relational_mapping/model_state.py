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


from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State Class that inherits from base linking to the states table
    class attribute id that represents a column of an auto-generated,
    unique integer, can't be null and is a primary key
    class attribute name that represents a column of a string
    with maximum 128 characters and can't be null"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
