#!/usr/bin/python3

"""Prints all City objects from the database hbtn_0e_14_usa:"""

from sqlalchemy.orm.session import Session
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
            f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    Base.metadata.create_all(engine)
    session = Session(engine)

    result = session.query(City, State).filter(City.state_id == State.id).all()
    for res in result:
        print(f'{res[1].name}: ({res[0].id}) {res[0].name}')
