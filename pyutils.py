"""
Utility methods and helper methods used around the project.
"""
import time
import datetime


def get_timestamp():
    """Gets a current timestamp with a global format."""
    # Create a timestamp
    timestamp = time.time()
    # Format the timestamp
    timestamp = datetime.datetime.fromtimestamp(timestamp).strftime(
        '%H:%M:%S')
    return timestamp
