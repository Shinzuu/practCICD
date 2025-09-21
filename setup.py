from setuptools import setup, find_packages

setup(
    name="todo_api",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.68.0",
        "uvicorn>=0.15.0",
        "pytest>=6.0.0",
        "httpx>=0.23.0",
    ],
)
