#!/usr/bin/python3
"""Define class BaseModel."""
import datetime
import uuid


class BaseModel:
    """BaseModel class."""

    def __init__(self, **kwargs):
        """Initialize class."""
        d_format = "%Y-%m-%dT%H:%M:%S.%f"
	if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'updated_at' or key == 'created_at':
                     self.__dict__[key] = datetime.datetime.strptime(value, d_format)
                else:
                    self.__dict__[key] = value
        else:
            self.id = uuid.uuid4()
	    self.created_at = datetime.datetime.now()

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
        this_dict["updated_at"] = datetime.datetime.now().isoformat()
        this_dict["created_at"] = datetime.datetime.now().isoformat()

        return this_dict
