import argparse
from inspyctor.review import review_code


def main():
    """Entry point for the CLI."""
    parser = argparse.ArgumentParser(description="Review Python code for style and security issues.")
    parser.add_argument('command', choices=['review'], help="Command to execute")
    parser.add_argument('file_path', help="Path to the Python file to review")

    args = parser.parse_args()

    if args.command == 'review':
        file_path = args.file_path
        try:
            with open(file_path, 'r'):
                pass  # Check if the file exists and is readable
            results = review_code(file_path)
            print("\n=== inspyctor Review ===\n")
            for category, feedback in results.items():
                print(f"{category}:\n{feedback}\n")
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
