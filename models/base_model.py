#!/usr/bin/python3
"""Define class BaseModel."""
import datetime
import uuid
import models


class BaseModel:
    """BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Initialize class."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

        d = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            keys = []
            for k in kwargs.keys():
                keys.append(k)
            if 'id' not in keys:
                self.id = str(uuid.uuid4())
            for key, value in kwargs.items():
                if key == 'updated_at' or key == 'created_at':
                    value = datetime.datetime.strptime(value, d)
                    if key != '__class__':
                        setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()

    def __str__(self):
        """Represent as string."""
        c = self.__class__.__name__
        return "[{}] ({}) {}".format(c, self.id, self.__dict__)

    def save(self):
        """Update."""
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert to dictionary."""
        this_dict = self.__dict__.copy()
        this_dict['__class__'] = self.__class__.__name__
        this_dict["updated_at"] = datetime.datetime.now().isoformat()
        this_dict["created_at"] = datetime.datetime.now().isoformat()

        return this_dict
