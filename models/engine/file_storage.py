#!/usr/bin/python3

"""
This module defines a class to manage file storage for hbnb clone
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class FileStorage:
    """
    This class manages storage of hbnb models in JSON format

    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """
        Returns a dictionary of models currently in storage
        """

        dct = {}  # Moved dictionary up
        if cls:
            dictionary = self.__objects
            for key in dictionary:
                partition = key.replace(".", " ")
                partition = shlex.split(partition)
                if (partition[0] == cls.__name__):
                    dct[key] = self.__objects[key]
            return dct
        else:
            return self.__objects

    def new(self, obj):
        """
        Adds new object to storage dictionary

        Args:
            obj: Object
        """

        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """
        Saves storage dictionary to file
        """

        temp = {}
        for key, val in self.__objects.items():
            temp[key] = val.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""

        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, val in (json.load(f)).items():
                    val = eval(val["__class__"]) (**val)
                    self.__objects[key] = val
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deleting an existing element
        """

        if obj:
            obj_key = "{}.{}".format(type(obj_key).__name__, obj.id)
            del self.__objects[obj_key]

    def close(self):
        """
        Calling reload()
        """
        self.reload()
