#!/usr/bin/python3
"""
This is the "place" module.
It supplies one class, Place.
"""

from models.base_model import BaseModel
import models
import json
import uuid
from datetime import datetime
import sys


class Place(BaseModel):
    """
    Place class
    """
    city_id = ""                # string - empty string: it will be the City.id
    user_id = ""                # string - empty string: it will be the User.id
    name = ""                   # string - empty string
    description = ""           # string - empty string
    number_rooms = int(0)       # integer - 0
    number_bathrooms = int(0)   # integer - 0
    max_guest = int(0)          # integer - 0
    price_by_night = int(0)     # integer - 0
    latitude = float(0.0)       # float - 0.0
    longitude = float(0.0)       # float - 0.0
    amenity_ids = []            # list of string - empty list: it will
    # be the list of Amenity.id later

    def __init__(self, *args, **kwargs):
        """constructor"""
        super().__init__(*args, **kwargs)
