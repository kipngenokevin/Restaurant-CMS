#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage


storage_type = os.environ.get('REST_TYPE_STORAGE', 'db')

if storage_type == 'file':
    storage = FileStorage()
else:
    storage = DBStorage()

"""Always reload after instantiation"""
storage.reload()
