#!/usr/bin/python3
"""
A script that adds the state object "Louisiana"  to the database htbn_0e_6_usa
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

    # create an object then add it
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    # print output
    print(new_state.id)

    # closing session
    session.close()
