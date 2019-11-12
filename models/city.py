#!/usr/bin/python3
"""
This is the "city" module.
It supplies one class, City.
"""

from models.base_model import BaseModel
import models
import json
import uuid
from datetime import datetime
import sys


class City(BaseModel):
    """
    City class
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """constructor"""
        super().__init__(*args, **kwargs)
