#!/usr/bin/python3
"""A script that deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pre_pool_ping=True)

    # create a session
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # retrieve states with letter 'a' in them
    states_wth_a = session.query(State).filter(State.name.like('%a%'))

    # delete the states
    for state in states_wth_a:
        session.delete(state)

    # commit and close the session
    session.commit()
    session.close()
