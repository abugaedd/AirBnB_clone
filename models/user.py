#!/usr/bin/python
""" holds class User"""
dels.base_model import BaseModel
from models.base_model import BaseModel
    """Representation of a user """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
