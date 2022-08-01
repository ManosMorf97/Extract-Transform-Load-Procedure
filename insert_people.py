from unittest import result
from neo4j import GraphDatabase
import mysql.connector
import mysql.connector.errorcode
import secretP
from secretP import *

names=["Albert","Bob","George","Dwayne","Eric","John","Teo","Bruce","Peter","David"]
surname="Doe"
names2=["Alice","Lisa","Floor","Jasmine","Fiona","Kate","Cameron","Olivia","Pamela","Mary"]
surname2="Puf"

Begin()

def Begin():
    data_base_connection = GraphDatabase.driver(uri = "bolt://localhost:7687",
    auth=("neo4j",neo4j_pwd))
    session = data_base_connection.session()
    print("Connection Done")
    prepare_graph_data(session)

def prepare_graph_data(session):
    cursor=mysql_connection()
    create_nodes(session,cursor,names,surname,1)
    create_nodes(session,cursor,names,surname2,11)


    
def mysql_connection():
    try:
        db=mysql.connector.connect(user='newuser',database='Manos',
        password=mysql_pwd,host="localhost")
    except mysql.connector.Error as err:
        print(err)
        return
    cursor=db.cursor()
    return cursor

def create_nodes(session,cursor,names,surname,begining_id):
    for i,name in zip(range(begining_id,10+begining_id),names):
        value='%'+i
        cursor.execute("select deviceID from devices where deviceID=%s",value)
        result=cursor.fetchall()
        for row in result:
            #row is the id at this case
            #continue
