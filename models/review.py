#!/usr/bin/python3

from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review

    Attributes:
    place_id: string - empty string (this will be the Place.id)
    user_id: string - empty string (this will be the User.id)
    text: string - empty string

    """

    place_id = ""
    user_id = ""
    text = ""

