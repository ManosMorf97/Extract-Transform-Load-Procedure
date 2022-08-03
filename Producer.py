import mysql.connector
import mysql.connector.errorcode
from urllib3 import add_stderr_logger
import secretP
from secretP import *
from kafka import KafkaProducer
from kafka.errors import KafkaError
import json

def Begin():
    try:
        db=mysql.connector.connect(user='newuser',database='Manos',
        password=mysql_pwd,host="localhost")
        send_data(db)
    except mysql.connector.Error as err:
        print(err)
        return
    

def get_data(db):
    cursor=db.cursor()
    cursor.execute("select * from products")
    results=[result for result in list(cursor.fetchall())]
    cursor.close()
    db.close()
    json_results=[json.dumps(result) for result in results]
    print(json_results)
    #send_data(results)

def send_data(results):
    kafka_producer=KafkaProducer(
        bootstrap_servers=['broker:1111'],
        batch_size=16384/200*10,
        linger_ms=20*1000
    )
    #6.40
    json_results=[json.dumps(result) for result in results]
    kafka_producer.send("products-topic",json_results)
    

    return

Begin()