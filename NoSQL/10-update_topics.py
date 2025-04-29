#!/usr/bin/env python3
"""
Module to update topics of a school document in MongoDB.
"""
from typing import List


def update_topics(mongo_collection, name: str, topics: List[str]) -> None:
    """
    Update the topics of a school document in MongoDB.

    Args:
        mongo_collection: The pymongo collection object
        name (str): The school name to update
        topics (list): The list of topics to set
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    ) 