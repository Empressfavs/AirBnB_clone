#!/usr/bin/python3


import uuid
from datetime import datetime


"""
Defines common attributes for all other classes
"""


class BaseModel:
    """
    Represents base model with common attributes and methods
    """
    def __init__(self):
        """Initializes instance attribute"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update_time(self):
        """Updates the update_at attribute with the current datetime"""
        self.update_at = datetime.now()

    def save(self):
        """update the updated_at attribute with the current datetime"""
        self.update_time()

    def to_dict(self):
        """converts the instance attributes to a dictionary.
        Dictionary containing all keys/values of __dict__ of the instance
        """
        object_dict = self.__dict__.copy()
        object_dict['__class__'] = self.__class__.__name__
        object_dict['created_at'] = self.created_at.isoformat()
        object_dict['updated_at'] = self.updated_at.isoformat()
        return object_dict

    def __str__(self):
        """provides a string representation of the object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
