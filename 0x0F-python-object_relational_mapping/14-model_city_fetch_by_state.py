#!/usr/bin/python3
"""Fetch States Module"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import urllib.parse

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1],
            urllib.parse.quote_plus(sys.argv[2]),
            # sys.argv[2],
            sys.argv[3],
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    Session = Session()
    cities = (
        Session.query(City, State).filter(
            City.state_id == State.id).order_by(City.id)
    )
    if cities:
        for city, state in cities:
            print("{}: ({}) {}".format(state.name, city.id, city.name))
