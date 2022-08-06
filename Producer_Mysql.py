from base64 import encode
import mysql.connector
import mysql.connector.errorcode
from urllib3 import add_stderr_logger
import secretP
from secretP import *
from kafka import KafkaProducer
import sys
import time
import json

def Begin():
    try:
        db=mysql.connector.connect(user='newuser',database='Manos',
        password=mysql_pwd,host="localhost")
        get_data(db)
        print("Done")
    except mysql.connector.Error as err:
        print(err)
        return
    

def get_data(db):
    cursor=db.cursor()
    cursor.execute("select * from products")
    results=[result for result in list(cursor.fetchall())]
    cursor.close()
    db.close()
    json_results=list(map(lambda result:{"productID":result[0],"type_product":result[1],
        "brand_company":result[2]},results))
    
    send_data(json_results,sys.getsizeof(json_results[0]))

def send_data(json_results,b_size):
    kafka_producer=KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        #batch_size=b_size,
        #linger_ms=5,
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )
    #6.40
    #400
    for result in json_results:
        kafka_producer.send("products-topic",result)
        time.sleep(2)

Begin()
