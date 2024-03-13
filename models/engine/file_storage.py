#!/usr/bin/python3
"""Filestorage class defined."""
import datetime
import json
import os


class FileStorage:

    """represents an abstracted storage engine.

    Attributes:
        __file_path (str): file to save objects to.
        __objects (dict): the dictionary of instantiated objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """set in __objects with key <obj_class_name>.id"""
        objname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(objname, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Reloads the stored objects"""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
