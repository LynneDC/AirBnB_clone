#!/usr/bin/python3
""" importing json module and"""
import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}
    def all(self):
        return self.__objects
    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
    def save(self):
        data = {}
        for key, value in self.__objects.items():
            data[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(data, file)
    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split(".")
                    cls = globals() [class_name]
                    obj = cls(**value)
                    self.__objects[key] = obj
        except (FileNotFoundError, json.JSONDecodeError):
            self.__objects = {}
