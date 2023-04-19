#!/usr/bin/python3
"""
A script that changes the name ofState object from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == '__main__':
    engine = create_engine('mysql://{username}:{password}@localhost:3306/
                          {db_name}'.format(sys.argv[1], sys.argv[2],
                          sys.argv[3]),
                          pool_pre_ping=True)

    Base.metadata.create_all(engine)

    # creating a session
    Sessionmaker = sessionmaker(bind=engine)
    session = Session()

    # query the state object of id=2
    state_id2 = session.query(State).filter_by(id=2).first()
    state_id2.name ="New Mexico"
    
    # commit
    session.commit()

    # closing session
    session.close()

