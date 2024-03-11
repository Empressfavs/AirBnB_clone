#!/usr/bin/python3
import uuid
from datetime import datetime


"""A class called Basemodel"""


class BaseModel:
    """a class BaseModel that defines all common attributes/methods
    for other classes
    """
    def __init__(self):
        """
        Constructor method for BaseModel class"
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Method to update the updated_at attribute with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Method to convert the instance attributes to a dictionary"""
        object_dict = self.__dict__.copy()
        object_dict['__class__'] = self.__class__.__name__
        object_dict['created_at'] = self.created_at.isoformat()
        object_dict['updated_at'] = self.updated_at.isoformat()
        return object_dict

    def __str__(self):
        """Method to provide a string representation of the object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

