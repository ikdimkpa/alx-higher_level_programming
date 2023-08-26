#!/usr/bin/python3
"""
This script lists all State objects, and corresponding City objects
contained in the database hbtn_0e_101_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm impoer sessionmaker
from relationship_state import State
from relationship_city import Base, City
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id)

    for state in states:
        print("{}:{}".format(state.id, state.name))
        for city in states.city:
            print("  {}:{}".format(city.id, city.name))

    session.close()
