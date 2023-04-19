#!/usr/bin/python3
"""
Script that prints the first state object from the database hbtn_0e_6_usa
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

    # querying the first state object
    state = session.query(State).order_by(State.id.asc()).first()

    if state is None:
        print('Nothing')

    else:
        print('{}: {}'.format(state.id, state.name))

    # closing session
    session.close()
