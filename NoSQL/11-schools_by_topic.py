#!/usr/bin/env python3
"""
Module to find schools by topic in MongoDB.
"""
from typing import List, Dict


def schools_by_topic(mongo_collection, topic: str) -> List[Dict]:
    """
    Find schools that have a specific topic.

    Args:
        mongo_collection: The pymongo collection object
        topic (str): The topic to search for

    Returns:
        A list of schools that have the specified topic
    """
    return list(mongo_collection.find({"topics": topic})) 