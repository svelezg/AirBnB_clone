#!/usr/bin/python3
"""
This is the "state" module.
It supplies one class, State.
"""

from models.base_model import BaseModel
import models
import json
import uuid
from datetime import datetime
import sys


class State(BaseModel):
    """
    State class
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """constructor"""
        super().__init__(*args, **kwargs)
