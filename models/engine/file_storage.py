"""File Storage."""
import json
from models.base_model import BaseModel


class FileStorage():
    """Serialize  instances to a JSON file and deserializes."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return dictionary of objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <class name>.id>."""
        class_name = obj.__class__.__name__
        obj_key = "{}.{}".format(class_name, obj.id)
        self.__objects[obj_key] = obj

    def save(self):
        """Serialize __objects to the file."""
        ser_obj = {}
        with open(FileStorage.__file_path, 'w') as f:
            for key, value in FileStorage.__objects.items():
                ser_obj[key] = value.to_dict()

            json.dump(ser_obj, f)

    def reload(self):
        """Deserialize the json file to __objects if file exists."""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                data = json.load(f)
                for key, val in data.items():
                    self.__objects[key] = eval(val['__class__'])(**val)

        except FileNotFoundError:
            pass
