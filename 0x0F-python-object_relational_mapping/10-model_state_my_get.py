#!/usr/bin/python3
"""Fetch States Module"""
import sys
from model_state import Base, State
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
    states = Session.query(State).filter_by(
        name=sys.argv[4]).order_by(State.id)
    if states:
        for state in states:
            print("{}".format(state.id))
    else:
        print("Not found")
