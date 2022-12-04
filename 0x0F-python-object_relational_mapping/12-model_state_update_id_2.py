#!/usr/bin/python3

"""
Print State object with the name passed.
as argument from the database hbtn_0e_6_usa.
"""
from sqlalchemy.orm.session import Session
from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
            f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    Base.metadata.create_all(engine)
    session = Session(engine)

    state = session.query(State).filter(State.id == 2).first()

    if state:
        state.name = 'New Mexico'
        session.commit()
