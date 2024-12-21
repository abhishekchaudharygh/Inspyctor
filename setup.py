# setup.py
from setuptools import setup, find_packages

setup(
    name="inspyctor",
    version="0.1.0",
    author="Abhishek Chaudhary",
    author_email="abhishekchaudhary1403@gmail.com",
    description="A Python package for code review using AI models and static analysis.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "transformers",
        "torch",
        "flake8",
        "bandit",
    ],
    entry_points={
        "console_scripts": [
            "inspyctor=inspyctor:review_code",
        ],
    },
    python_requires=">=3.7",
)
