#!/usr/bin/python3
"""
Starts the engine, creates the table and query the table
"""
from mysqlalchemy import create_engine
from mysqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
            .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(City, States)
    states = query.filter(City.state_id == State.id).order_by(City.id)

    for city, state in states:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
