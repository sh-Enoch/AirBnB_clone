#!/usr/bin/python3
"""Class FileStorage."""


class FileStorage:
    """Define class FileStorage."""

    __file_path = file_path
    __objects = {}
    def all(self):
        """Return dictionary of __objects."""
        return self.__objects
    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        my_dict = self.__objects
        id = str(uuid.uuid4())
        my_dict["{}.{}".format(type(self)__name__, id)] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        my_dict =  self.__objects
        my_obj = {}
        for key, value in my_dict.items():
            my_obj[key] = value.to_dict()
        my_obj_serialized = dump(my_obj)
        with open(self.__file_path, 'w') as file:
            file.write(my_obj_serialized)

    def  reload(self):
        """Deserialize the JSONfile to __objects only if __file_path exists."""
        pass

