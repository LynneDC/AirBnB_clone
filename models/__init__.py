#!/usr/bin/python3
""" import storagemodule from models that is and link BaseModel with filestorage
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
