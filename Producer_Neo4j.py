from neo4j import GraphDatabase
from urllib3 import add_stderr_logger
import secretP
from secretP import *
from kafka import KafkaProducer
from kafka.errors import KafkaError
import json
import sys
import time

data_base_connection = GraphDatabase.driver(uri = "bolt://localhost:7687",
    auth=("neo4j",neo4j_pwd))
print("Connection Done")
session=data_base_connection.session()
results=session.run("Match(n) Return(n)")
json_results = [j[0]._properties for j in results]
session.close()
data_base_connection.close()
b_size=sys.getsizeof(json_results)
kafka_producer=KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )
seconds=time.time()
for result in json_results:
    kafka_producer.send("users-topic",result)
    time.sleep(4)
print(time.time()-seconds)



