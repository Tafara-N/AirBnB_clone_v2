#!/usr/bin/python3

"""
Place class
"""

from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """
    Place class

    Attributes:
        city_id: City's id
        user_id: User's id
        name: Name input
        description: Description of the place
        number_rooms: Number of rooms (int)
        number_bathrooms: Number of bathrooms (int)
        max_guest: Maximum guest (int)
        price_by_night: Price for a stay (int)
        latitude: Latitude (float)
        longitude: Longitude (float)
        amenity_ids: List of Amenity ids
    """

    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade='all, delete, delete-orphan',
                               backref="place")

        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            """
            Returns a list of reviews.id
            """

            var = models.storage.all()
            our_list = []
            result = []
            for key in var:
                review = key.replace('.', ' ')
                review = shlex.split(review)
                if (review[0] == 'Review'):
                    our_list.append(var[key])
            for element in our_list:
                if (element.place_id == self.id):
                    result.append(element)
            return (result)

        @property
        def amenities(self):
            """ Returns a list of amenity ids """

            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """
            Appends amenity ids to the attribute
            """

            if type(obj) is Amenity and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
