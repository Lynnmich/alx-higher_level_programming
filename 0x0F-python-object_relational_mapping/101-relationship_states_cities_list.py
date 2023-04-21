#!/usr/bin/python3
"""
A script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa.
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # creating session
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # querying the session
    states = session.query(State).order_by(State.id).all()

    # print output
    for state in states:
        print('{}:'.format(state_name))
        for city in state.cities:
            print('\t{}: {}'.format(city.id, city.name))

    # closing session
    session.close()
