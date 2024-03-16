#!/usr/bin/python3
"""
Script that changes the name of a State object
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
    state_to_update = session.query(State).filter(State.id == 2).first()
    if state_to_update:
        state_to_update.name = 'New Mexico'
        session.commit()
    session.close()
