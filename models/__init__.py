#!/usr/bin/python3
"""Initialize the models package and create the storage singleton."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
