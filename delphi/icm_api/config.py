from pathlib import Path

# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os

BASE_DIR = Path(__file__).parent

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = f"sqlite:///{BASE_DIR}/delphi.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2
