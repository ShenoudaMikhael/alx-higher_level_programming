#!/usr/bin/python3
"""Model State Module"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """States Class Model"""

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
