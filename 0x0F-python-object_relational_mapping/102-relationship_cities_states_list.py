#!/usr/bin/python3
"""Fetch States Module"""
import sys
from relationship_city import Base, City
from relationship_state import State

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
    cts = Session.query(City).all()
    for ct in cts:
        print("{}: {} -> {}".format(ct.id, ct.name, ct.state.name))
