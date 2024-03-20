#!/usr/bin/python3

"""
This module defines a base class for all models in our hbnb clone
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
import uuid
import models

Base = declarative_base()


class BaseModel:
    """ A base class for all hbnb models """
# Added the "created_at/updated_at", they were missing
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))

    def __init__(self, *args, **kwargs):
        """
        Instantiates a new model

        Args:
            args: Will not be used
            kwargs: For the constructor of the BaseModel
        Attributes:
            id: unique id generated
            created_at: creation date
            updated_at: updated date
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the instance
        """
        # Testing if this works, if not, put the original back
        # cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(type(self).__name__,
                                    self.id, self.__dict__)

    def __repr__(self):  # Added __repr__ method
        """
        Returns a string representaion
        """
        return self.__str__()

    def save(self):
        """
        Updates updated_at with current time when instance is changed
        """

        from models import storage

        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):  # Updated this: added "_sa_instance_state and"
        # update "created_at/updated_at" methods
        """
        Converts instances into dictionary format
        """

        dictionary = dict(self.__dict__)
        dictionary["__class__"] = str(type(self).__name__)
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()

        if '_sa_instance_state' in dictionary.keys():
            del dictionary['_sa_instance_state']

        return dictionary

    def delete(self):
        """ Deleting the object """
        models.storage.delete(self)
