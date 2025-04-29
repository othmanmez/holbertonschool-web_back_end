#!/usr/bin/env python3
"""
Module to provide statistics about Nginx logs stored in MongoDB.
"""
from pymongo import MongoClient


def log_stats():
    """
    Provide statistics about Nginx logs stored in MongoDB.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    # Count total logs
    total_logs = logs_collection.count_documents({})
    print(f"{total_logs} logs")

    # Count logs by method
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = logs_collection.count_documents({"method": method})
        print(f"    method {method}: {count}")

    # Count logs with method=GET and path=/status
    status_count = logs_collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_count} status check")


if __name__ == "__main__":
    log_stats() 