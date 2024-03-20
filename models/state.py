#!/usr/bin/python3

"""
The State class for the HBNB project
"""

from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import shlex


class State(BaseModel, Base):
    """
    State class

    Attributes:
        name: Input name
    """

    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        '''
        Returns the list of City instances with state_id
                equals the current State.id
                Returns FileStorage relationship between State and City
        '''

        var = models.storage.all()
        our_list = []
        related_cities = []
        for key in var:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                our_list.append(var[key])
        for element in our_list:
            if (element.state_id == self.id):
                related_cities.append(element)
        return (related_cities)
