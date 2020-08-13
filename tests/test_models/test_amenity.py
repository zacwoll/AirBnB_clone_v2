#!/usr/bin/python3
"""test amenity module"""
import unittest
from io import StringIO
import pep8
import os
import json
import console
import tests
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import *
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from os import getenv


class TestAmenity(unittest.TestCase):
    """ class for testing amenity"""

    def __init__(self, *args, **kwargs):
        """ init method"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ is name a str """
        new = self.value()
        self.assertEqual(new.name, "")

    def test_pep8_amenity(self):
        """Pep8 amenity file"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["models/amenity.py"])
        self.assertEqual(p.total_errors, 0, 'fix Pep8')

    def test_docstrings_in_amenity(self):
        """ check for docs in amenity """
        self.assertIsNotNone(Amenity.__doc__)


if __name__ == "__main__":
    unittest.main()
