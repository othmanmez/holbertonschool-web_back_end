#!/usr/bin/env python3
"""
Module to insert a document into a MongoDB collection.
"""
from typing import Dict, Any


def insert_school(mongo_collection, **kwargs) -> str:
    """
    Insert a new document into a MongoDB collection.

    Args:
        mongo_collection: The pymongo collection object
        **kwargs: The document fields to insert

    Returns:
        The _id of the inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id 