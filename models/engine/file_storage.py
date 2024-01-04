#!/usr/bin/python3
"""Class FileStorage."""
import json
from models.base_model import BaseModel
import models


class FileStorage:
    """Defines the class FileStorage."""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects  to json file_path."""
        this_dict = {}

        for key in self.__objects:
            this_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(this_dict, file)

    def reload(self):
        """Deserialize the Json file to __objects."""
        try:
            with open(self.__file_path, 'r', encoding='UTF8') as file:
                this_new_dict = json.load(file)

            for value in this_new_dict.values():
                class_name = value["__class__"]
                del value["__class__"]
                self.new(eval(class_name)(**value))
        except FileNotFoundError:
            pass
