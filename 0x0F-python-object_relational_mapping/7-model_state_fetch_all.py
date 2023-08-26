#!/usr/bin/python3
"""

"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3]))

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


