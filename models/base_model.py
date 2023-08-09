#!/usr/bin/python3
""" model base """
import models
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Base Class"""

    def __init__(self, *args, **kwargs):
        """ constructor """

        if kwargs:
            """ dictionary representation """
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == '__class__':
                    continue
                else:
                    setattr(self, key, value)
        else:
            """ new instance """
            self.id = str(uuid4())
            self.updated_at = datetime.now()
            self.created_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """" return de representation of the instance """
        nameClass = self.__class__.__name__
        return "[{}] ({}) {}".format(nameClass, self.id, self.__dict__)

    def save(self):
        """ save the changes and update the date """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ to dict() """

        dictionary = {}
        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                dictionary[key] = value.isoformat()
            else:
                dictionary[key] = value
        dictionary['__class__'] = self.__class__.__name__

        return dictionary
