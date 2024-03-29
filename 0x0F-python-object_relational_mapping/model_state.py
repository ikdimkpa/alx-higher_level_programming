#!/usr/bin/python3
""" Defines a class named State
    Inherits from SQLAlchemy Base and links to the table states of MySQL
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Contains the class definition of a State and an
    instance Base = declarative_base():"""

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
