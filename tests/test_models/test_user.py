#!/usr/bin/python3
"""Unit tests for the User class."""
import unittest

from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def test_inherits_from_base_model(self):
        self.assertTrue(issubclass(User, BaseModel))

    def test_class_attributes_default_to_empty_strings(self):
        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")

    def test_instance_attribute_assignment(self):
        user = User()
        user.email = "a@b.com"
        user.first_name = "Ada"
        self.assertEqual(user.email, "a@b.com")
        self.assertEqual(user.first_name, "Ada")

    def test_to_dict_class_name(self):
        self.assertEqual(User().to_dict()["__class__"], "User")


if __name__ == "__main__":
    unittest.main()
