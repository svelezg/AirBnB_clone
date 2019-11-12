#!/usr/bin/python3
"""
This is the "amenity" module.
It supplies one class, Amenity.
"""

from models.base_model import BaseModel
import models
import json
import uuid
from datetime import datetime
import sys


class Amenity(BaseModel):
    """
    Amenity class
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """constructor"""
        super().__init__(*args, **kwargs)
