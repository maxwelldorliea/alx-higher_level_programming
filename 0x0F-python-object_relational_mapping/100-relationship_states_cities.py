#!/usr/bin/python3

"""
Creates the State “California” with the City.
“San Francisco” from the database hbtn_0e_100_usa.
"""
from sys import argv
from sqlalchemy.orm import session
from sqlalchemy.orm.session import Session
from sqlalchemy import create_engine
from relationship_city import Base, City
from relationship_state import State

if __name__ == '__main__':
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    Base.metadata.create_all(engine)
    session = Session(engine)

    n_state = State(name="California")
    n_state.cities = [City(name='San Francisco')]
    session.add(n_state)
    session.commit()
