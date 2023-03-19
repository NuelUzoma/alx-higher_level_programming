#!/usr/bin/python3
"""Write a script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa
Your script should take 4 arguments: mysql username,
mysql password, database name and state name to search (SQL injection free)
You must use the module SQLAlchemy
You must import State and Base from model_state -
from model_state import Base, State
Your script should connect to a MySQL server running on
localhost at port 3306
Results must be sorted in ascending order by states.id
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
                           .format(USR, PWD, DB), echo=True)
    engine.connect()
    Base.metatdata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    list_state = session.query(State).filter(State.name == sys.argv[4]
                                             ).order_by(State.id)
    print(list_state)
    session.commit()
    session.close()
