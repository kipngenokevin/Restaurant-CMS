#!/usr/bin/python3
"""Init module for model package"""
from models.engine.file_storage import FileStorage


"""create the variable storage, an instance of FileStorage"""
storage = FileStorage()
"""call reload() method on this variable"""
storage.reload()
