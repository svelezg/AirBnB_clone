#!/usr/bin/python3
"""
This is the "user" module.
It supplies one class, user.
"""

from models.base_model import BaseModel
import models
import json
import uuid
from datetime import datetime
import sys


class User(BaseModel):
    """
    User class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
