#!/usr/bin/python3
"""
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

    #querying the first state object
    states = session.query(State).order_by(State.id.asc()).first()

    if state is None:
    print('Nothing')
    
    else:

    print(f'{state.id}: {state.name}')

    #closing session
    session.close()
