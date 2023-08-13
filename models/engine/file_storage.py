#!/usr/bin/python3
"""Module for FileStorage class."""
import json

class FileStorage:
    """Class for serializtion and deserialization of base classes."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns __objects dictionary."""
        # TODO: should this be a copy()?
        return self.__objects

    def new(self, obj):
        """Sets new obj in __objects dictionary."""
        # TODO: should these be more precise specifiers?
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialzes __objects to JSON file."""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(serialized_objects, file)


    def reload(self):
        """Returns a dictionary of valid classes and their references."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        
        class_mapping = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }
        """Deserializes JSON file into __objects."""

        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    class_name = obj_dict["__class__"]
                    class_object = class_mapping[class_name]
                    obj = class_object(**obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

