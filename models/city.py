#!/usr/bin/python3
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city

    Attributes:
        state_id: string - empty string (this will be the State.id)
        name: string - empty string
    """

    state_id = ""
    name = ""

