#!/usr/bin/python3
"""Class FileStorage."""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
import os


class FileStorage:
    """Define class FileStorage."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return dictionary of __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        my_dict = self.__objects
        id = str(uuid.uuid4())
        my_dict["{}.{}".format(type(self).__name__, id)] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        my_dict = self.__objects
        my_obj = {}

        for key, value in my_dict.items():
            my_obj[key] = value.to_dict()
        my_obj_serialized = dump(my_obj)
        with open(self.__file_path, 'w') as file:
            json.dump(my_obj_serialized, file)

    def reload(self):
        """Deserialize the JSONfile to __objects only if __file_path exists."""
        try:
            with open(FileStorage.__file_path) as file:
                obj = json.load(file)
            for key, value in obj.items():
                class_name = value['__class__']
                class_obj = globals()[class_name]
                instance = class_obj(**value)
                self.new(instance)

        except FileNotFoundError:
            pass
