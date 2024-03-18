#!/usr/bin/python3
"""
This module contains
class FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances.
"""
import json
from os.path import exists


class FileStorage:
    """
    serializes instances to a JSON file
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        when this method is called:
        - it takes self.__objects dictionary the it loops through
        for every value of the __objects dictionary, it passes the method
        to_dict() from the BaseModel class
        This returns the dictionary representation that can be passed onto JSON
        otherwise, without this method, it will pass its memory reference alone
        which will cause an error.
        After this, it dumps the dictionary into a file using json.dump
        """
        serialized_objs = {}
        for key, value in self.__objects.items():
            serialized_objs[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objs, file)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        otherwise do nothing
        If the file doesn’t exist, no exception should be raised)

        __objects look like this:

        {"BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d": {"my_number": 89,
        "__class__": "BaseModel", "updated_at": "2017-09-28T21:07:25.047381",
        "created_at": "2017-09-28T21:07:25.047372", "name": "My_First_Model",
        "id": "ee49c413-023a-4b49-bd28-f2936c95460d"}}
        """
        if exists(self.__file_path):
            from models.base_model import BaseModel
            with open(self.__file_path, 'r') as file:
                loaded_objs = json.load(file)
                self.__objects = loaded_objs
            new_objects = {}
            for key, value in self.__objects.items():
                class_name, obj_id = key.split('.')
                if class_name == 'BaseModel':
                    new_instance = BaseModel(**value)
                new_objects[key] = new_instance
            self.__objects = new_objects
        else:
            pass
