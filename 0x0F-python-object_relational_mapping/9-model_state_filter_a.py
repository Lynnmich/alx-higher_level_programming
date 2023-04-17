#!/usr/bin/python3
""" A script that prints all the states with letter 'a' from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ = '__main__':

    engine = create_engine('mysql://{username}:{password}@localhost:3306/{db_name}'.format(argv[1], argv[2], argv[3]))

    #creating a session
    Session = sessionmaker(bind=engine)
    session = Session()

    #querying the states with letter 'a'
    states = session.query(State).filter(State.name.like('%a%')).orderby(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    #closing session
    session.close()
