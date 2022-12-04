#!/usr/bin/python3

"""City Model Module."""

from sqlalchemy.sql.schema import ForeignKey
from model_state import Base, State
from sqlalchemy import Column, String, Integer


class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('State.id'))
