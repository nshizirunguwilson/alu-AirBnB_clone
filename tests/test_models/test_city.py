#!/usr/bin/python3
"""Unit tests for the City class."""
import unittest

from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def test_inherits_from_base_model(self):
        self.assertTrue(issubclass(City, BaseModel))

    def test_class_attributes(self):
        self.assertEqual(City.state_id, "")
        self.assertEqual(City.name, "")

    def test_instance_attribute_assignment(self):
        city = City()
        city.name = "Kigali"
        city.state_id = "abc"
        self.assertEqual(city.name, "Kigali")
        self.assertEqual(city.state_id, "abc")

    def test_to_dict_class_name(self):
        self.assertEqual(City().to_dict()["__class__"], "City")


if __name__ == "__main__":
    unittest.main()
