from pymongo import MongoClient
from datetime import datetime
from config import SONET_ENVIRONMENT, SONET_MONGO_USER, SONET_MONGO_PASSWORD

if SONET_ENVIRONMENT is 'prod':
    uri = "mongodb://{0}:{1}@10.240.0.4:27017/sonet"
    client = MongoClient(uri.format(SONET_MONGO_USER, SONET_MONGO_PASSWORD))
else:
    client = MongoClient()

db = client.sonet
