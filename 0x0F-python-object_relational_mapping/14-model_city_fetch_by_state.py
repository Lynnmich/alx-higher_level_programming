#!/usr/bin/python3
"""
 a Python file similar to model_state.py named model_city.py
 that contains the class definition of a City.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import Base, City

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    # creating a session
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve all cities
    cities = session.query(State, City).filter(State.id == City.state_id)

    # print all cities
    for c in cities:
        print("{}: ({}) {}".format(c.State.name, c.City.id, c.City.name))

    # closing session
    session.close()
