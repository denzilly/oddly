import mysql.connector
from mysql.connector import Error
from configparser import ConfigParser
import os




def db_connect(db, local=False):

    config = ConfigParser()
    config.read(f'{os.getcwd()}/modules/config.ini')

    if local:
        host = "192.168.1.4"
    else:
        host = config.get('main','server')


    try:
        connection = mysql.connector.connect(host=host,
                                            database=db,
                                            user=config.get('main','user'),
                                            password=config.get('main','pass'),
                                            pool_name="bartpool",
                                            pool_size=4,
                                            buffered=True
        )
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            cursor.close()

    except Error as e:
        print("Error while connecting to MySQL", e)
    

    return connection



def db_close(connection):
    
    connection.close()
    print("connection closed")