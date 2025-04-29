#!/usr/bin/env python3
"""
Module to list all documents in a MongoDB collection.
"""
from typing import List, Dict


def list_all(mongo_collection) -> List[Dict]:
    """
    List all documents in a MongoDB collection.

    Args:
        mongo_collection: The pymongo collection object

    Returns:
        A list of all documents in the collection
    """
    return list(mongo_collection.find()) 