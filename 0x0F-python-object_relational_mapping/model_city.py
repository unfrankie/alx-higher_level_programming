#!/usr/bin/python3
"""
Contains the class definition of a City and an
instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """City class"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(ForeignKey('states.id'), nullable=False)
