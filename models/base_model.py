#!/usr/bin/python3
""" import the module """
import uuid
from datetime import datetime
""" define the class """
class BaseModel:
    """ instances """
    
    def __init__(self, *args, **kwargs): 
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.today()
                else:
                    self.__dict__[k] = v
    """ function for string output """
    def __str__(self):
        str(self.id)
        return f"[{__class__.__name__}] ({self.id}) {vars(self)}"
    
    """ updating instance updated_at """
    def save(self):
        self.updated_at = datetime.now()

    """ dict output """
    def to_dict(self):
        d1 = { "__class__" : __class__.__name__}
        self.__dict__.update(d1)
        self.created_at = self.created_at.isoformat(sep='T', timespec='auto')
        self.updated_at = self.updated_at.isoformat(sep='T', timespec='auto')
        return self.__dict__

