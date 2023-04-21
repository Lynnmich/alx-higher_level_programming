#!/usr/bin/python3
"""
A script that lists all City objects from the database hbtn_0e_101_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # create a session
    Base.metadata(create_all)
    Session = sessionmaker(bind=engine)
    session = Session()

    # querying the session
    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print('{}: ({}) {}'.format(city.id, city.name, state.name))

    # closing session
    session.close()
