#!/usr/bin/python3
"""
Script to export data in CSV format
"""

import csv
import json
import requests
import sys


def get_employee_tasks(employee_id):
    """Get employee tasks from API"""
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    return response.json()


def get_employee_info(employee_id):
    """Get employee information from API"""
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    return response.json()


def export_to_csv(employee_id):
    """Export employee tasks to CSV file"""
    # Get employee info and tasks
    employee = get_employee_info(employee_id)
    tasks = get_employee_tasks(employee_id)

    # Prepare CSV filename
    filename = f"{employee_id}.csv"

    # Write to CSV file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([
                employee_id,
                employee.get('username'),
                task.get('completed'),
                task.get('title')
            ])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 4-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        export_to_csv(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1) 