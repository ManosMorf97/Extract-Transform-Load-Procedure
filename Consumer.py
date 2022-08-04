from kafka import KafkaConsumer
from kafka.errors import KafkaError
import json
import pymongo
import secretP
from secretP import *

def get_database():
    from pymongo import MongoClient
    import pymongo

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://Manos97:"
    CONNECTION_STRING+=mongodb_pwd
    CONNECTION_STRING+="@clusterm1997.zpbgesp.mongodb.net/?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['UsersAndProducts']
    
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":    
    
    # Get the database
    dbname = get_database()

print("Mongo Done")


def decoder(m):
    return json.loads(m.decode('ascii'))

consumerSQL=KafkaConsumer(
    'products-topic',
	bootstrap_servers=['localhost:9092'],
	auto_offset_reset='earliest',
    value_deserializer=decoder,
    consumer_timeout_ms=3000
)
for message in consumerSQL:
    print(message.value)

consumerNeo4j=KafkaConsumer(
    'users-topic',
	bootstrap_servers=['localhost:9092'],
	auto_offset_reset='earliest',
    value_deserializer=decoder,
    consumer_timeout_ms=3000
)

for message in consumerNeo4j:
    print(message.value)



