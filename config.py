import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(os.path.join('.env'))

TOKEN=os.environ.get('TOKEN')