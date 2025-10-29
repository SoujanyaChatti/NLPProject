import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def get_database():
    DATABASE_URL = os.getenv("DATABASE_URL")
    client = MongoClient(DATABASE_URL)
    return client.get_database()
