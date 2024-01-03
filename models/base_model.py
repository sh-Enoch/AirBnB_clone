#!/usr/bin/python3
"""Define class BaseModel."""
import datetime
import uuid


class BaseModel:
    """BaseModel class."""

    def __init__(self):
        """Initialize class."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Represent as string."""
        c = type(self).__name__
        return "[{}] ({}) {}".format(c, self.id, self.__dict__)

    def save(self):
        """Update."""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Convert to dictionary."""
        this_dict = self.__dict__
        this_dict['__class__'] = type(self).__name__
        for key, value in this_dict.items():
            this_dict["updated_at"] = datetime.datetime.now().isoformat()
            this_dict["created_at"] = datetime.datetime.now().isoformat()

        return this_dict
