import mysql.connector
import mysql.connector.errorcode
from urllib3 import add_stderr_logger
import secretP
from secretP import *

def prepare_mysql_connection():
    try:
        db=mysql.connector.connect(user='newuser',database='Manos',
        password=mysql_pwd,host="localhost")
    except mysql.connector.Error as err:
        print(err)
        return
    prepare_mysql_data(db)

def prepare_mysql_data(db):
    try:
        TABLES={}
        #TABLES['devices']=
        cursor=db.cursor()
        sql_statement=("CREATE TABLE IF NOT EXISTS 'devices' ("
            "'deviceID' varchar(3) not null",
            "'TYPEdevice' varchar(20) not null",
            "'BRANDcompany' varchar(20) not null",
            "primary key(deviceID)"
            ")ENGINE=InnoDB")
        cursor.execute(sql_statement)
        cursor.flush()
        db.commit()
        types=['mobile_phone','television','microwave','dishwaser','clock',
            'electric_grill','oven','laptop','camera','webcam']
        brand='samsung'
        for type in types:
            for i in range(1,10):
                sql_statement=("Insert into table 'devices'"
                    "values({},{},{})".format(type+str(i),type,brand))
                cursor.execute(sql_statement)
                cursor.flush()
                db.commit() 
        print("Done")
    except mysql.connector.Error as err:
        print(err)
        print("O")
    cursor.close()
    db.close()
    return

prepare_mysql_connection()
