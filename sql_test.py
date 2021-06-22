import mysql.connector
from mysql.connector import Error
from configparser import ConfigParser
import os


config = ConfigParser()
config.read(f'{os.getcwd()}/modules/config.ini')


connection = mysql.connector.connect(host="192.168.1.22",
                                            database="market_DB",
                                            user=config.get('main','user'),
                                            password=config.get('main','pass'),
                                            pool_name="bartpool",
                                            pool_size=4,
                                            buffered=True,
                                            auth_plugin='mysql_native_password'
)
if connection.is_connected():
    db_Info = connection.get_server_info()
    print("Connected to MySQL Server version ", db_Info)
    cursor = connection.cursor()
    cursor.execute("select database();")
    record = cursor.fetchone()
    print("You're connected to database: ", record)
    cursor.close()

