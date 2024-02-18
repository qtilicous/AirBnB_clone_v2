#!/usr/bin/python3
"""This module defines the FileStorage class."""
import json
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to a JSON and deserializes JSON to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON to __objects if JSON (__file_path) exists"""
        try:
            with open(
                    FileStorage.__file_path, mode="r", encoding="utf-8"
                    ) as f:
                FileStorage.__objects = json.load(f)
                for key, value in FileStorage.__objects.items():
                    cls_name = value['__class__']
                    del value['__class__']
                    self.new(eval(cls_name)(**value))
        except FileNotFoundError:
            pass

    def close(self):
        """Call reload() method for deserializing the JSON file to objects"""
        self.reload()
