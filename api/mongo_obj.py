from pymongo import MongoClient
import os

client = None

def fetch_singleton():
    global client
    if client is None:
        mongo_host = os.environ.get('DB_HOST')
        mongo_port = int(os.environ.get('DB_PORT'))
        client = MongoClient(mongo_host, mongo_port, maxPoolSize=50)
    return client
