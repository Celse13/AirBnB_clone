#!/usr/bin/python3
"""init FileStorage"""
from .base_model import BaseModel
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
