#!/usr/bin/python3
"""Write a script that prints the
first State object from the database hbtn_0e_6_usa
Your script should take 3 arguments: mysql username,
mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state -
from model_state import Base, State
Your script should connect to a MySQL server running on
localhost at port 3306
You are not allowed to fetch all states from the database
before printing the first one
"""
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    USR = sys.argv[1]
    PWD = sys.argv[2]
    DB = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(USR, PWD, DB), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    first_state = session.query(State).order_by(State.id).first()
    if first_state is not None:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")
    session.close()
