#!/usr/bin/python3
"""
Import the `uuid` class for generating unique IDs
Import the `datetime` class for representing the datetime of UUID creation
"""
import uuid
from models import storage
from datetime import datetime

"""
Def class BaseModel parent class for all attributes and methods.
Public instance attributes:
    - `id`: assigned with a UUID on creation
    - `created_at`: current datetime of ID creation
    - `updated_at`: current time of ID update
Output format: [class_name] (id) dict
Public instance methods:
    - `save()`: updates `updated_at` with the current date
    - `to_dict()`: returns a dictionary representation of the instance:
        - `self.__dict__`: returns only the instance attributes
        - `__class__`: added to the dictionary with the class name
        - `created_at` and `updated_at`: converted to ISO format
    - `object_dict`: dictionary representation of the instance
"""


class BaseModel:
    """Class initialization and data declaration"""
    def __init__(self, *args, **kwargs):
        # If keyword arguments are provided
        if kwargs:
            for key, value in kwargs.items():
                # Exclude the "__class__" attribute
                if key != "__class__":
                    if isinstance(value, str):
                        # Convert "created_at" and "updated_at"
                        # strings to datetime objects
                        if key in ["created_at", "updated_at"]:
                            value = datetime.strptime(
                                value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            # Generate a new UUID for the "id" attribute
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    """Public methods to modify public instance attributes"""
    def save(self):
        self.updated_at = datetime.now()
        storage.save()
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__

        if isinstance(obj_dict["created_at"], datetime):
            # Convert "created_at" to ISO format
            obj_dict["created_at"] = obj_dict["created_at"].isoformat()

        if isinstance(obj_dict["updated_at"], datetime):
            # Convert "updated_at" to ISO format
            obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()
        return obj_dict

    def __str__(self):
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
