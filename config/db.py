from pymongo import MongoClient
import pymongo
import os
from dotenv import load_dotenv

load_dotenv()
MONGO_URL = os.getenv("MONGO_URL")
conn  = MongoClient(MONGO_URL)
db = conn["pdfai"]
users_collection = db["users"]
try: 
    connection = conn.server_info()
    print("Connected to MongoDB " + str(connection.get("version")))
except pymongo.errors.ServerSelectionTimeoutError as err:
    print(err)
    print("Could not connect to MongoDB")
