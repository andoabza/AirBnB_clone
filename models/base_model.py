#!/usr/bin/python3
import uuid
from datetime import datetime
""" import the modules """
class BaseModel:
    def __init__(self):
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"{__class__.__name__} {self.id} {self.__dict__}"
    def save(self):
        self.updated_at = datetime.now()
    def to_dict(self):
        return self.__dict__

