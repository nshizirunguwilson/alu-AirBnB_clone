#!/usr/bin/python3
"""Unit tests for the Amenity class."""
import unittest

from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def test_inherits_from_base_model(self):
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_class_attribute_name(self):
        self.assertEqual(Amenity.name, "")

    def test_instance_attribute_assignment(self):
        amenity = Amenity()
        amenity.name = "Wi-Fi"
        self.assertEqual(amenity.name, "Wi-Fi")

    def test_to_dict_class_name(self):
        self.assertEqual(Amenity().to_dict()["__class__"], "Amenity")


if __name__ == "__main__":
    unittest.main()
