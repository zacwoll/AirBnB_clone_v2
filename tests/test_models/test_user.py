#!/usr/bin/python3
""" a module for user tests"""
import unittest
import pep8
from models.user import User


class TestUser(unittest.TestCase):
    """ a class for user tests"""

    def __init__(self, *args, **kwargs):
        """ init method """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_pep8_user(self):
        """tests for pep8 """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["user.py"])
        self.assertEqual(p.total_errors, 0, 'fix Pep8')

    def test_docs_user(self):
        """ check for docstrings """
        self.assertIsNotNone(User.__doc__)

    def test_first_name(self):
        """ is first name a str"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ is last name a str"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ is email a str"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ is pwd a str"""
        new = self.value()
        self.assertEqual(type(new.password), str)


if __name__ == "__main__":
    unittest.main()
