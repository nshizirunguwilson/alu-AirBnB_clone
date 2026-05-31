#!/usr/bin/python3
"""Defines the BaseModel class for the AirBnB clone project."""
import uuid
from datetime import datetime


class BaseModel:
    """Base class that defines common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance.

        When kwargs is provided, recreate the instance from a dictionary
        representation; otherwise generate a new id and timestamps and
        register the instance with the storage engine.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at") and isinstance(
                        value, str):
                    try:
                        value = datetime.fromisoformat(value)
                    except (ValueError, AttributeError):
                        value = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models import storage
            storage.new(self)

    def __str__(self):
        """Return the informal string representation of the instance."""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at and persist the change through storage."""
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        result = self.__dict__.copy()
        result["__class__"] = type(self).__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result
