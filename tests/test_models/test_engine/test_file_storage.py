#!/usr/bin/python3
"""Unit tests for the FileStorage engine."""
import json
import os
import unittest

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        """Reset the in-memory store and remove any persisted file."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """Clean up the persisted JSON file between tests."""
        if os.path.isfile("file.json"):
            os.remove("file.json")

    def test_storage_is_file_storage_instance(self):
        self.assertIsInstance(storage, FileStorage)

    def test_all_returns_dict(self):
        self.assertIsInstance(storage.all(), dict)

    def test_new_registers_object(self):
        model = BaseModel()
        key = "BaseModel.{}".format(model.id)
        self.assertIn(key, storage.all())
        self.assertIs(storage.all()[key], model)

    def test_save_creates_json_file(self):
        BaseModel()
        storage.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_save_serializes_objects(self):
        model = BaseModel()
        storage.save()
        with open("file.json", "r", encoding="utf-8") as fp:
            data = json.load(fp)
        self.assertIn("BaseModel.{}".format(model.id), data)

    def test_reload_restores_objects(self):
        model = BaseModel()
        storage.save()
        FileStorage._FileStorage__objects = {}
        storage.reload()
        self.assertIn("BaseModel.{}".format(model.id), storage.all())

    def test_reload_without_file_does_not_raise(self):
        storage.reload()


if __name__ == "__main__":
    unittest.main()
