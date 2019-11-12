#!/usr/bin/python3
"""
This is the "review" module.
It supplies one class, Review.
"""

from models.base_model import BaseModel
import models
import json
import uuid
from datetime import datetime
import sys


class Review(BaseModel):
    """
    Review class
    """
    place_id = ""
    user_id = ""
    text = ""


def __init__(self, *args, **kwargs):
    """constructor"""
    super().__init__(*args, **kwargs)
