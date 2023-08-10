#!/usr/bin/python3
""" storage model """
import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """FileStorage class"""

    """private class attributes"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ return a dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """ set the dictionary """
        nameClass = obj.__class__.__name__
        idClass = obj.id
        key = nameClass+'.'+idClass
        FileStorage.__objects[key] = obj

    def save(self):
        """ serialize the object to a JSON file"""
        data = {}
        for key, value in FileStorage.__objects.items():
            data.update({key: value.to_dict()})
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file)

    def reload(self):
        """ deserialize the JSON file into a python object"""
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8')as file:
                data = {}
                data = json.load(file)
                for key, value in data.items():
                    val = value['__class__']
                    FileStorage.__objects[key] = globals()[val](**value)
