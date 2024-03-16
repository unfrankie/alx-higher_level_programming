#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    url_database = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
    engine = create_engine(url_database)
    Session = sessionmaker(bind=engine)
    session = Session()
    states_delete = session.query(State).filter(State.name.like('%a%')).all()
    for state in states_delete:
        session.delete(state)
    session.commit()
    session.close()
