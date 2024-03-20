#!/usr/bin/python3

"""
The State class for the HBNB project
"""

from models import storage_type
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.city import City

class State(BaseModel, Base):
    """
    State class

    Attributes:
        name: input name
    """

    __tablename__ = "states"
    if storage_type == 'db':
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
else:
    name = ''

    @property
    def cities(self):
            '''Returns the list of City instances with state_id
                equals the current State.id
                Returns FileStorage relationship between State and City
            '''
            from models import storage
            related_cities = []
            cities = storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    related_cities.append(city)
            return related_cities
