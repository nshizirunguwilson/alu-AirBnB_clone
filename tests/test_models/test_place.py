#!/usr/bin/python3
"""Unit tests for the Place class."""
import unittest

from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

    def test_inherits_from_base_model(self):
        self.assertTrue(issubclass(Place, BaseModel))

    def test_default_class_attributes(self):
        self.assertEqual(Place.city_id, "")
        self.assertEqual(Place.user_id, "")
        self.assertEqual(Place.name, "")
        self.assertEqual(Place.description, "")
        self.assertEqual(Place.number_rooms, 0)
        self.assertEqual(Place.number_bathrooms, 0)
        self.assertEqual(Place.max_guest, 0)
        self.assertEqual(Place.price_by_night, 0)
        self.assertEqual(Place.latitude, 0.0)
        self.assertEqual(Place.longitude, 0.0)
        self.assertEqual(Place.amenity_ids, [])

    def test_instance_attribute_assignment(self):
        place = Place()
        place.name = "Cozy"
        place.number_rooms = 2
        self.assertEqual(place.name, "Cozy")
        self.assertEqual(place.number_rooms, 2)

    def test_to_dict_class_name(self):
        self.assertEqual(Place().to_dict()["__class__"], "Place")


if __name__ == "__main__":
    unittest.main()
