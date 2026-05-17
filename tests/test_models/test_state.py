#!/usr/bin/python3
"""Unit tests for the State class."""
import unittest

from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def test_inherits_from_base_model(self):
        self.assertTrue(issubclass(State, BaseModel))

    def test_class_attribute_name(self):
        self.assertEqual(State.name, "")

    def test_instance_attribute_assignment(self):
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")

    def test_to_dict_class_name(self):
        self.assertEqual(State().to_dict()["__class__"], "State")


if __name__ == "__main__":
    unittest.main()
