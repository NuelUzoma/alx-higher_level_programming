#!/usr/bin/python3
"""Write a script that lists all State objects from the database hbtn_0e_6_usa
        Your script should take 3 arguments: mysql username,
        mysql password and database name
        You must use the module SQLAlchemy
        You must import State and Base from model_state -
        from model_state import Base, State
        Your script should connect to a MySQL server running on
        localhost at port 3306
        Results must be sorted in ascending order by states.id"""


import model_state
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=model_state.engine)
session = Session()


def model_state_fetch_all():
    """A function to query using SQLAlchemy module to send queries"""

    for instance in session.query(State).order_by(State.id):
        print("{}: {}".format(instance.id, instance.name))


if __name__ == "__main__":
    model_state_fetch_all()
