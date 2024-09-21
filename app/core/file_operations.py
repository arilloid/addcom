import sys
import os


def load_contents(filepath):
    """
    Read the contents of a file and return it. If the file is not found,
    print an error message and return None.
    """
    if not os.path.isfile(filepath):
        print(f"File not found: {filepath}", file=sys.stderr)
        return None
    
    with open(filepath, 'r') as file:
        return file.read()