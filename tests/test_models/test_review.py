#!/usr/bin/python3
""" module for tests on Review """
import unittest
import pep8
from models.review import Review


class TestReview(unittest.TestCase):
    """ tests for review"""

    def __init__(self, *args, **kwargs):
        """ init method """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_pep8_review(self):
        """check for pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["review.py"])
        self.assertEqual(p.total_errors, 0, 'fix Pep8')

    def test_docs_review(self):
        """ check for docstrings """
        self.assertIsNotNone(Review.__doc__)

    def test_place_id(self):
        """ place id"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ user id"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ test test """
        new = self.value()
        self.assertEqual(type(new.text), str)


if __name__ == "__main__":
            unittest.main()
