#!/usr/bin/python3
"""Write a script that lists all State objects from the database hbtn_0e_6_usa
Your script should take 3 arguments: mysql username,
mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state -
from model_state import Base, State
Your script should connect to a MySQL server running on
localhost at port 3306
Results must be sorted in ascending order by states.id
"""


if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    import sys

    USR = sys.argv[1]
    PWD = sys.argv[2]
    DB = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(USR, PWD, DB), echo=True)
    engine.connect()
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).order_by(State.id):
        print("{}: {}".format(instance.id, instance.name))
    session.commit()
    session.close()
