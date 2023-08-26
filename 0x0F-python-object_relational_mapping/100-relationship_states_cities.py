#!/usr/bin/python3
"""
This script creates the State “California” with the City “San Francisco”
    from the database hbtn_0e_100_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
            .format(argv[1], argv[2], argv[3]))
    
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(State(name='California', cities[City(name='San Francisco')]))
    session.commit()

    session.close()
