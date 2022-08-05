import secretP
from secretP import *

def get_database():
    from pymongo import MongoClient

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://Manos97:"
    CONNECTION_STRING+=mongodb_pwd
    CONNECTION_STRING+="@clusterm1997.zpbgesp.mongodb.net/?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    db=client["UsersAndProducts"]
    return db
