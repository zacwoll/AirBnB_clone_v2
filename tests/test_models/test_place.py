#!/usr/bin/python3
""" module for place tests """
import unittest
import pep8
from models.place import Place


class test_Place(unittest.TestCase):
    """ class for testing Place"""

    def __init__(self, *args, **kwargs):
        """ init method"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_pep8_place(self):
        """is it pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["models/place.py"])
        self.assertEqual(p.total_errors, 0, 'fix Pep8')

    def test_docs_place(self):
        """check for docstrings """
        self.assertIsNotNone(Place.__doc__)

    def test_city_id(self):
        """ is id a str"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ is user id a thing"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ is name a str"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ is description"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ is no of rooms"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ is # of bathrooms"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ maximum guest"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ price by night"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ latitude"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ longitude"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ amenity ids"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)


if __name__ == "__main__":
    unittest.main()
