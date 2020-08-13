#!/usr/bin/python3
""" module for state reviews"""
import unittest
import pep8
from models.state import Place
from models.base_model import BaseModel
import os

class TestPlace(unittest.TestCase):
    """ a class for testing Place"""

    @classmethod
    def setUpClass(cls):
        """ Example Data """
        cls.place = Place()
        cls.place.city_id = "san-francisco"
        cls.place.user_id = "madame-tabitha"
        cls.place.name = "Gilded Lily"
        cls.place.description = "A fragrant paradise where flowers bloom"
        cls.place.number_rooms = 30
        cls.place.number_bathrooms = 5
        cls.place.max_guest = 3
        cls.place.price_by_night = 500
        cls.place.latitude = 37.77
        cls.place.longitude = 122.42
        cls.place.amenity_ids = ["1324-asdf"]

    @classmethod
    def teardown(cls):
        """ tear down Class """
        del cls.state

    def tearDown(self):
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_Place_pep8(self):
        """check for pep8 """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["models/state.py"])
        self.assertEqual(p.total_errors, 0, 'fix Pep8')

    def test_Place_docs(self):
        """ check for docstring """
        self.assertIsNotNone(Place.__doc__)

    def test_Place_attribute_types(self):
        """ test Place attribute types """
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(self.place.amenity_ids), list)

    def test_Place_is_subclass(self):
        """ test if Place is subclass of BaseModel """
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_Place_save(self):
        """ test save() command """
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state_updated_at)

    def test_Place_sa_instance_state(self):
        """ test is _sa_instance_state has been removed """
        self.assertNotIn('_sa_instance_state', self.state.to_dict())

if __name__ == "__main__":
    unittest.main()
