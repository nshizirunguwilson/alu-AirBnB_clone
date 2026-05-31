#!/usr/bin/python3
"""Unit tests for the BaseModel class."""
import json
import os
import unittest
import uuid
from datetime import datetime
from time import sleep

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_instance_creation(self):
        """A BaseModel instance is created with required attributes."""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_id_is_valid_uuid(self):
        """The id attribute is a valid uuid4 string."""
        model = BaseModel()
        uuid.UUID(model.id)

    def test_unique_ids(self):
        """Two BaseModel instances have different ids."""
        self.assertNotEqual(BaseModel().id, BaseModel().id)

    def test_str_representation(self):
        """__str__ returns the expected format."""
        model = BaseModel()
        expected = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(str(model), expected)

    def test_save_updates_updated_at(self):
        """save() refreshes the updated_at timestamp."""
        model = BaseModel()
        first = model.updated_at
        sleep(0.01)
        model.save()
        self.assertGreater(model.updated_at, first)

    def test_save_persists_to_storage(self):
        """save() persists the instance to the JSON file via storage."""
        if os.path.isfile("file.json"):
            os.remove("file.json")
        model = BaseModel()
        model.save()
        self.assertTrue(os.path.isfile("file.json"))
        with open("file.json", "r", encoding="utf-8") as fp:
            data = json.load(fp)
        self.assertIn("BaseModel.{}".format(model.id), data)

    def test_to_dict_contains_class_key(self):
        """to_dict includes __class__ with the class name."""
        model = BaseModel()
        data = model.to_dict()
        self.assertEqual(data["__class__"], "BaseModel")

    def test_to_dict_iso_format(self):
        """to_dict serializes datetime attributes to ISO format strings."""
        model = BaseModel()
        data = model.to_dict()
        self.assertEqual(data["created_at"], model.created_at.isoformat())
        self.assertEqual(data["updated_at"], model.updated_at.isoformat())

    def test_to_dict_returns_copy(self):
        """to_dict does not return the instance's __dict__ object."""
        model = BaseModel()
        self.assertIsNot(model.to_dict(), model.__dict__)


if __name__ == "__main__":
    unittest.main()
