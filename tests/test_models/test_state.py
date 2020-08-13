#!/usr/bin/python3
""" module for state reviews"""
import unittest
import pep8
from models.state import State


class TestState(unittest.TestCase):
    """ a class for testing State"""

    def __init__(self, *args, **kwargs):
        """ init method """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_pep8_state(self):
        """check for pep8 """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["state.py"])
        self.assertEqual(p.total_errors, 0, 'fix Pep8')

    def test_docs_state(self):
        """ check for docstring """
        self.assertIsNotNone(State.__doc__)

    def test_name3(self):
        """ is name a str """
        new = State()
        self.assertEqual(type(new.name), str)


if __name__ == "__main__":
    unittest.main()
