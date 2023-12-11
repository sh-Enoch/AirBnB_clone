#!/usr/bin/python3
"""Class BaseModel."""
import uuid
from datetime import datetime


class BaseModel:
    """Define class BaseModel."""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel class."""
        if kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.name = args[0] if args else ""
            self.my_number = args[1] if len(args) > 1 else 0

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if "created_at" in kwargs:
            t = strptime(kwargs["created_at"], "%Y-%m-%d %H:%M:%S")
            self.created_at = datetime.t
        if "updated_at" in kwargs:
            x = strptime(kwargs["updated_at"], "%Y-%m-%d %H:%M:%S")
            self.updated_at = datetime.x

    def __str__(self):
        """Return a  simple representation of my class."""
        val = type(self).__name__
        return "[{} ({}) {}]".format(val, self.id, self.__dict__)

    def save(self):
        """Update datetime with current datetime."""
        self.updated_at = datetime.now()
        return self.__dict__

    def to_dict(self):
        """Return a dictionary with all key/value."""
        self.__dict__['__class__'] = type(self).__name__
        my_dict = self.__dict__
        my_dict['updated_at'] = datetime.now().isoformat()
        my_dict['created_at'] = datetime.now().isoformat()
        return my_dict
