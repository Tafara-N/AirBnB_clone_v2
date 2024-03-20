#!/usr/bin/python3

"""
The City class  for the HBNB project
"""

from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place


class City(BaseModel, Base):
    """
    City class

    Attributes:
        state_id: The state id
        name: input name
    """

    __tablename__ = "cities"

    # if storage_type == 'db':
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship('Place', backref='cities',
                                cascade='all, delete, delete-orphan')

    # else:
    #     name = ''
    #     state_id = ''
