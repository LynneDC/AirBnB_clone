#!/usr/bin/python3

from models.base_model import BaseModel


class Place(BaseModel):
    """Inherits from BaseModel class

    Attributes:
        city_id: string - empty string (this will be the City.id)
        user_id: string - empty string (this will be the User.id)
        name: string - empty string
        description: string - empty string
        number_rooms: integer - 0
        number_bathrooms: integer - 0
        max_guest: integer - 0
        price_by_night: integer - 0
        latitude: float - 0.0
        longitude: float - 0.0
        amenity_ids: list of string - empty list (this will be the list of Amenity.id later)

    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

