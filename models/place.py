#!/usr/bin/python3
"""import BaseModel module"""
from models.base_model import BaseModel
"""define class that inhert from BaseModel"""
class Place(BaseModel):
    """class atrributes"""
    city_id = " "
    user_id = " "
    name = " "
    discription = " "
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

