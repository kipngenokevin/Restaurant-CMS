#!/usr/bin/python3
"""
This is the basemodel for all classes
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Basemodel is inherited by all other class.
    It has the attributes id, created_at, updated_at
    """

    def __init__(self, *args, **kwargs):
        """Initilizes public instance attributes:
        id - string - assign with an uuid when an instance is created
        created_at: datetime - assign with the current datetime
        when an instance is created
        updated_at: datetime - assign with the current datetime
        it will be updated every time you change your object
        """
        if kwargs:
            if '__class__' in kwargs:
                del kwargs['__class__']
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        should print: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__)

    def save(self):
        """
        updates the public instance attribute updated_at with the current
        date & time
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary of all the values containing
        all keys/values
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
