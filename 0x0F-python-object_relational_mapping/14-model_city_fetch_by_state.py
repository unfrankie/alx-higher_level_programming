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
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    url_database = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
    engine = create_engine(url_database)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))
    session.close()
