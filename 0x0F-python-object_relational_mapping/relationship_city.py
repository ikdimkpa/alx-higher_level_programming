#!/usr/bin/python3
"""
Create a model for the city table
"""
from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base

class City(Base):
    """Schema for the City table
    __table__name(String): MySQL table that stores Cities
    id (sqlalchemy.Integer): id of the city
    name (sqlalchemy.String): name of the city
    state_id (sqlalchemy.Integer): states's id
    """
    __tablename__ = "city"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"))
