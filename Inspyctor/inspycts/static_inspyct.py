import subprocess


def run_flake8(file_path):
    """Running Flake8 for PEP8 style checking."""
    result = subprocess.run(['flake8', file_path], capture_output=True, text=True)
    return result.stdout


def run_bandit(file_path):
    """Running Bandit for security analysis."""
    result = subprocess.run(['bandit', '-r', file_path], capture_output=True, text=True)
    return result.stdout
