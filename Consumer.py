from kafka import KafkaConsumer
from kafka.errors import KafkaError
import json
from connection_to_mongodb import *


def decoder(m):
    return json.loads(m.decode('ascii'))

def binarySearch(arr, x):
    l = 0
    r = len(arr)
    while (l <= r):
        m = l + ((r - l) // 2)
 
        if x == arr[m]['productID']:
            return m
        # If x greater, ignore left half
        elif x>arr[m]['productID']:
            l = m + 1
 
        # If x is smaller, ignore right half
        else:
            r = m - 1
 
    return -1

db=get_database()
collection =db['Users_Products']

consumerSQL=KafkaConsumer(
    'products-topic',
	bootstrap_servers=['localhost:9092'],
	auto_offset_reset='earliest',
    value_deserializer=decoder,
    consumer_timeout_ms=3000
)
products=[message.value for message in consumerSQL]

consumerNeo4j=KafkaConsumer(
    'users-topic',
	bootstrap_servers=['localhost:9092'],
	auto_offset_reset='earliest',
    value_deserializer=decoder,
    consumer_timeout_ms=3000
)

people=[message.value for message in consumerNeo4j]
   
products=sorted(products, key=lambda p: p['productID'])

for person in people:
    dict_of_products=None
    dict_of_products=[]
    for productID in person['products']:
        index=binarySearch(products,productID)
        dict_of_products.append(products[index])
    person['products']=[]
    person['products']=dict_of_products
    with open(person['full_name']+".json", "w") as outfile:
        json.dump(person,outfile)
    collection.insert_one(person)
print("DONE")


