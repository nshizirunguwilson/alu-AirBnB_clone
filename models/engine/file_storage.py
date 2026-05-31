#!/usr/bin/python3
"""Defines the FileStorage class used to persist instances to a JSON file."""
import json
import os


class FileStorage:
    """Serializes instances to a JSON file and deserializes them back."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of stored objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Add obj to the storage dictionary keyed by <class name>.<id>."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        serializable = {
            key: obj.to_dict()
            for key, obj in FileStorage.__objects.items()
        }
        with open(FileStorage.__file_path, "w", encoding="utf-8") as fp:
            json.dump(serializable, fp)

    def reload(self):
        """Deserialize the JSON file into __objects if it exists."""
        if not os.path.isfile(FileStorage.__file_path):
            return
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
        }
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as fp:
                data = json.load(fp)
        except (json.JSONDecodeError, OSError):
            return
        for key, value in data.items():
            if not isinstance(value, dict):
                continue
            cls = classes.get(value.get("__class__"))
            if cls is None:
                continue
            try:
                FileStorage.__objects[key] = cls(**value)
            except (TypeError, ValueError):
                continue
