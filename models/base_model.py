#!/usr/bin/python3
"""Class BaseModel."""
import uuid
from datetime import datetime


class BaseModel:
    """Define class BaseModel."""

    def __init__(self):
        """Initialize BaseModel class."""
        self.name = ""
        self.my_number = 0
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

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
