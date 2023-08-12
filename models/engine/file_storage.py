#!/usr/bin/python3
# Importing the json module
import json


class FileStorage:
    # Define the file path for storing data
    __file_path = "file.json"
    # Store objects in a dictionary
    __objects = {}

    def all(self):
        # Return all objects stored in the dictionary
        return FileStorage.__objects

    def new(self, obj):
        # Generate a key based on the class name and object ID
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        # Add the object to the dictionary using the generated key
        FileStorage.__objects[key] = obj

    def save(self):
        # Create an empty dictionary to store data
        data = {}
        # Iterate over the objects in the dictionary
        for key, value in FileStorage.__objects.items():
            # Convert each object to a dictionary representation
            data[key] = value.to_dict()
        # Write the data to the file in JSON format
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(data, file)

    def reload(self):
        # Import the BaseModel class
        from models.base_model import BaseModel
        # Define the mapping of class names to classes
        data_classes = {"BaseModel": BaseModel}
        try:
            # Open the file for reading
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                # Load the data from the file
                data = json.load(file)
                # Iterate over the values in the loaded data
                for values in data.values():
                    # Get the class name from the "__class__" attribute
                    name = values["__class__"]
                    # Get the corresponding class from the mapping
                    obj = data_classes[name]
                    # Create a new object and add it to the dictionary
                    self.new(obj(**values))
        except FileNotFoundError:
            # If the file is not found, return
            return
