import sqlite3
import os
import datetime
import time

try:
    connection = sqlite3.connect(os.getcwd()+'\data\odds_DB.db')
    cursor = connection.cursor()
    now = datetime.datetime.now()
    sqlite_select_Query = "select sqlite_version();"
      

    cursor.execute("""SELECT *
                        FROM ODDS_DATA
                        ORDER BY id DESC
                        LIMIT 1"""
                        )
    new_id = cursor.fetchall()[0][0] + 1
    print(new_id)


    # insert = f""" INSERT INTO ODDS_DATA(id,time,FRANCE,GERMANY,ENGLAND,BELGIUM,SPAIN,ITALY,PORTUGAL,NETHERLANDS,CROATIA,SWITZERLAND,DENMARK,UKRAINE,SWEDEN,AUSTRIA,POLAND,TURKEY,CZECH_REPUBLIC,WALES,SCOTLAND,RUSSIA,FINLAND,NORTH_MACEDONIA,HUNGARY,SLOVAKIA) 
    # VALUES(4,'{str(now)}',2,1,3,4,2,3,54,2,3,5,2,3,5,43,5,3,43,3,2,3,4,5,3,2)"""
    
    # cursor.execute(insert)
    # connection.commit()

    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)


finally:
    if connection:
        
        connection.close()
        print("The SQLite connection is closed")


# create table

