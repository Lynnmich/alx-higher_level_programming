#!/usr/bin/python3
"""
A script that adds the state object "Louisiana"  to the data base  htbn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine('mysql://{username}:{password}@localhost:3306/
                          {db_name}'.format(sys.argv[1], sys.argv[2], sys.argv[3])
                          pool_pre_ping=True)
    
    Base.metadata.create_all(engine)

    #creating a session
    Session = sessionmaker(bind=engine)
    session = Session()

    #create an object then add it
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    #print output
    print(new_state.id)

    #closing session
    session.close()
