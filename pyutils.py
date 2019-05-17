"""
Utility methods and helper methods used around the project.
"""
import datetime
import time
from pathlib import Path


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
    # print("Checking if filepath {} is a file".format(filepath))
    filepath = "{}".format(filepath)
    fl = Path(filepath)
    if fl.is_file():
        return True
    return False
