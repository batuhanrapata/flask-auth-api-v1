import os
from pymongo import MongoClient

MONGO_URI = os.getenv('MONGO_URI')
MONGO_DBNAME = os.getenv('MONGO_DBNAME')


def get_db(collection: str):
    """
    Get a database connection
    returns: pymongo.database.Database instance
    """
    client = MongoClient(MONGO_URI)
    db = client[MONGO_DBNAME]
    return db[collection]
