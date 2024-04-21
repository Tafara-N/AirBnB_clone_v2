#!/usr/bin/python3

"""
This module defines a class to manage file storage for hbnb clone
"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """
    Serializing instances to JSON file and
    deserializing them back to instances
    """
    __file_path = "file.json"  # String - JSON file path

    # Dictionary - Will store all objects by <class name>.id
    __objects = {}

    def all(self, cls=None):
        """
        Returns:
            dictionary __objects
        """

        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_obj = {}
        for key in self.__objects:
            json_obj[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(json_obj, f)

    def reload(self):
        """
        Deserializing JSON files to __objects
        """

        try:
            with open(self.__file_path, "r") as f:
                json_obj = json.load(f)
            for key in json_obj:
                self.__objects[key] = classes[json_obj[key]["__class__"]](
                    **json_obj[key])
        except:
            pass

    def delete(self, obj=None):
        """
        Delete obj from __objects if it"s inside
        """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """
        Calling reload() method to deserialize JSON files to objects
        """
        self.reload()
