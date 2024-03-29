#!/usr/bin/python3
"""
A script that prints all the states with
letter 'a' from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    # creating a session
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # querying the states with letter 'a' in them
    states = session.query(State).filter(State.name.like('%a%')) \
             .order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    # closing session
    session.close()
