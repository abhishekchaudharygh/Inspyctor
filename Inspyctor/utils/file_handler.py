import os


def read_code(file_path):
    """Read the code from a given file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} does not exist.")
    with open(file_path, 'r') as file:
        return file.read()
