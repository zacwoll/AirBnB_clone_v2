#!/usr/bin/python3
""" module for city tests"""
import unittest
import pep8
from models.city import City


class test_City(unittest.TestCase):
    """ class for testing city"""

    def __init__(self, *args, **kwargs):
        """ init method"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_docs_city(self):
        """check for docs"""
        self.assertIsNotNone(City.__doc__)

    def test_pep8_city(self):
        """check for pep8ness"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["city.py"])
        self.assertEqual(p.total_errors, 0, 'fix Pep8')

    def test_state_id(self):
        """ checking state id is a str"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ is name a string"""
        new = self.value()
        self.assertEqual(type(new.name), str)


if __name__ == "__main__":
    unittest.main()
