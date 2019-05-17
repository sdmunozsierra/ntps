"""
Utility methods and helper methods used around the project.
"""
import datetime
import os
import time


def get_timestamp():
    """Gets a current timestamp with a global format."""
    # Create a timestamp
    timestamp = time.time()
    # Format the timestamp
    timestamp = datetime.datetime.fromtimestamp(timestamp).strftime(
        '%H:%M:%S')
    return timestamp


def get_filename(directory):
    """Gets a filename from a specified directory."""
    pass


def check_file_exists(filepath):
    """Checks if the file exists."""
    if os.path.isfile(filepath):
        return True
    return False
