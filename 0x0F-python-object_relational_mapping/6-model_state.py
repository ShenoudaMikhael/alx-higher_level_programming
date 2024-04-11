#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
import urllib.parse

from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{username}:{password}@localhost/{database}".format(
            username=sys.argv[1],
            password=urllib.parse.quote_plus(sys.argv[2]),
            database=sys.argv[3],
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
