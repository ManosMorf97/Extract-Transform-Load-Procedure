from unittest import result
from neo4j import GraphDatabase
import mysql.connector
import mysql.connector.errorcode
import itertools
import secretP
from secretP import *

names=['Albert','Bob','George','Dwayne','Eric','John','Teo','Bruce','Peter','David']
surname='Doe'
names2=['Alice','Lisa','Floor','Jasmine','Fiona','Kate','Cameron','Olivia','Pamela','Mary']
surname2='Puf'


def Begin():
    data_base_connection = GraphDatabase.driver(uri = "bolt://localhost:7687",
    auth=("neo4j",neo4j_pwd))
    #session = data_base_connection.session()
    print("Connection Done")
    prepare_graph_data(data_base_connection)
    print("Done")

def prepare_graph_data(dbc):
    db=mysql_connection()
    create_nodes(dbc,db,names,surname,1,True)
    create_nodes(dbc,db,names2,surname2,11,False)
    for i in range(0,len(names)):
        full_name_male=names[i]+'_'+surname
        full_name_female=names2[i]+'_'+surname2
        make_friendship(full_name_male,full_name_female,dbc)
        make_friendship(full_name_female,full_name_male,dbc)


    
def mysql_connection():
    try:
        db=mysql.connector.connect(user='newuser',database='Manos',
        password=mysql_pwd,host="localhost")
    except mysql.connector.Error as err:
        print(err)
        return
    return db

def create_nodes(dbc,db,names,surname,begining_id,clean):
    cursor=db.cursor()
    session = dbc.session()
    if clean:
        session.run("MATCH (n) DETACH DELETE n")
    for i,name in zip(range(begining_id,10+begining_id),names):
        value=['%C'+str(i)]
        cursor.execute("select productID from products where productID like (%s)",value)
        results=[item for result in list(cursor.fetchall()) for item in result]
        full_name=name+'_'+surname
        command="CREATE("+full_name+":Person "
        command+="{full_name: '"+full_name+"', name: '"+name
        string_results="','".join(results)
        string_results="'"+string_results+"'"
        command+="' ,surname: '"+surname+"' , products: ["+string_results+"]})"
        session.run(command)
    session.close()
    cursor.close()
    full_names=list(map(lambda name:name+"_"+surname,names))
    for pair in itertools.product(full_names, repeat=2):
        if pair[0]==pair[1]:
            continue
        make_friendship(pair[0],pair[1],dbc)

def make_friendship(A,B,dbc):
    session = dbc.session()
    command="MATCH(a:Person),(b:Person) WHERE a.full_name = '"+A+"' AND b.full_name = '"+B+"'"
    command+="CREATE (a)-[:Has_Firend]->(b)"
    session.run(command)
    session.close()

Begin()