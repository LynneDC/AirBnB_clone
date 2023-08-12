#!/usr/bin/python3
""" import storagemodule from models that is and link BaseModel with filestorage
"""
from models.engine.file_storage import FileStorage
#from models.base_model import BaseModel

storage = FileStorage()
storage.reload()
