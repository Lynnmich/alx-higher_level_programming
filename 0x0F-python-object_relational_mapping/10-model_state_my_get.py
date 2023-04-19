#!/usr/bin/python3
"""
A script that prints State object with the name argument passed from
the database hbtn_oe_6_usa
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

    # querying the state object
    state = session.query(State).filter_by(name=sys.argv[4]).first()

    if state is None:
        print("Not found")

    else:
        print(state.id)

    # closing session
    session.close()
