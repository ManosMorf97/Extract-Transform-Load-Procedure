from flask import Flask
from connection_to_mongodb import *

def getUserProducts(full_name):
    db=get_database()
    collection=db['Users_Products']
    person=list(collection.find({'full_name':full_name}))[0]
    return person["products"]

print(getUserProducts("Albert_Doe"))