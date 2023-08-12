#!/usr/bin/python3
# importing json module and
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        data = {}
        for key, value in FileStorage.__objects.items():
            data[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(data, file)

    def reload(self):
        from models.base_model import BaseModel
        data_classes = {"BaseModel": BaseModel}
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                for values in data.values():
                    name = values["__class__"]

                    obj = data_classes[name]
                    self.new(obj(**values))
        except FileNotFoundError:
            return
