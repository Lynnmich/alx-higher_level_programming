#!/usr/bin/python3
"""
A script that lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ = '__main__:
    engine = create _engine('mysql://{username}:{password}@localhost:3306/{db_name}'.format(argv[1], argv[2], argv[3]))

    #creating a session
    Session = sessionmaker(bind=engine)
    session = Session()

    #querying all the state objects
    states = session.query(State).order_by(State.id.asc()).all()

    #printing all states
    for state in states:
    print(f'{state.id}: {state.name}')

    #closing session
    session.close()
