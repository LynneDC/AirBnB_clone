#!/usr/bin/python3
"""import class uuid for unique id
and datetime for datetimeof uuid creation
"""

import uuid
from models import storage
from datetime import datetime


"""
define a class basemodel that is
the parrent class to the all attribuets and
methods
puplic  instance attributes:
    id: is assigned with uuid on creation
    created_at: curret datime of id creation
    updated_at: curreect time of update id
output format: [class_name] (id) dict
public instance methods:
    save(): updates updated_at with current date
    to_dict(): returns dict uses:
        self.__dict__: return only inst attr
        __class__:added to dict with cls_name
        created_at & updated_at: converted to isoformat()
        [%Y-%m-%dT%H:%M:%S.%f for2017-06-14T22:31:03.285259
Return:
    object_dict
"""


class BaseModel:
    """ data declaration and initilization"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if isinstance(value, str):
                        if key in ["created_at", "updated_at"]:
                            value = datetime.strptime(
                                value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:

            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    """public methods to modify public instances"""
    def save(self):
        self.updated_at = datetime.now()

        storage.save()
        return "[{}] ({}) {}".format(
                        self.__class__.__name__,
                        self.id, self.__dict__)

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__

        if isinstance(obj_dict["created_at"], datetime):
            obj_dict["created_at"] = obj_dict["created_at"].isoformat()

        if isinstance(obj_dict["updated_at"], datetime):
            obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()
        return obj_dict

    def __str__(self):
        return "[{}] ({}) {}".format(
                        self.__class__.__name__,
                        self.id, self.__dict__)
