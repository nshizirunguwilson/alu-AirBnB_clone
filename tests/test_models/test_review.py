#!/usr/bin/python3
"""Unit tests for the Review class."""
import unittest

from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def test_inherits_from_base_model(self):
        self.assertTrue(issubclass(Review, BaseModel))

    def test_default_class_attributes(self):
        self.assertEqual(Review.place_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(Review.text, "")

    def test_instance_attribute_assignment(self):
        review = Review()
        review.text = "Great stay"
        self.assertEqual(review.text, "Great stay")

    def test_to_dict_class_name(self):
        self.assertEqual(Review().to_dict()["__class__"], "Review")


if __name__ == "__main__":
    unittest.main()
