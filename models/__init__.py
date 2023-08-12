#!/usr/bin/python3
"""
Import the `FileStorage` module from the `models.engine.file_storage` package
and link the `BaseModel` class with the `FileStorage` class.
"""
from models.engine.file_storage import FileStorage

# Create an instance of the `FileStorage` class
storage = FileStorage()

# Load data from the file into the `FileStorage` instance
storage.reload()
