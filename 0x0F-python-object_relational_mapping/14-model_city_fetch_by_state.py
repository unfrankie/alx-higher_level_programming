#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    url_database = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
    engine = create_engine(url_database)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State.name, City.id, City.name). \
        join(State, City.state_id == State.id).order_by(City.id)
    for state, id, city in result:
        print(f"{state}: ({id}) {city}")
    session.close()
