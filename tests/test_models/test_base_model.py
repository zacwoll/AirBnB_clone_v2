#!/usr/bin/python3
""" base model test module"""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os
import pep8


class test_basemodel(unittest.TestCase):
    """ a class for testing the base model """

    def __init__(self, *args, **kwargs):
        """ init method """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ set up """
        pass

    def tearDown(self):
        """ tear it down """
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_pep8_BaseModel(self):
        """ testing for pep8 """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstring_BaseModel(self):
        """checking for docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.new.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.delete.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_default(self):
        """ i am not sure what this test was for """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ i assume this is checking the kwargs"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ this is also a mystery test from the codebase"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ old test for str rep"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ test for dict """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ if there are no kwargs?"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ one kwarg """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """ making sure the id is a str? """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ datetime test"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ another datetime test"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertTrue(new.created_at != new.updated_at)
