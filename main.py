import pystore
import os
import pandas
import time
import datetime

import sqlite3


from xpaths import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options


### connect to the DB
try:
    connection = sqlite3.connect(os.getcwd()+'\data\odds_DB.db')
    cursor = connection.cursor()
    now = datetime.datetime.now()
    sqlite_select_Query = "select sqlite_version();"


except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)



options=Options()
options.headless = True


driver = webdriver.Firefox(options=options)
driver.get("https://www.paddypower.com/football/uefa-euro-2020?tab=outrights")

driver.execute_script("window.scrollTo(0, 500)")
time.sleep(3)
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, p_xpaths("none")["cookies"]))).click()


while True:
    

    
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, p_xpaths("none")["showall"]))).click()
    
    


    nr = {time : datetime.datetime.now()}
    for x in range(1,25):
        country = driver.find_element_by_xpath(p_xpaths(str(x))["country"]).get_attribute("innerHTML").upper().replace(" ","_")
        try:
            odds = driver.find_element_by_xpath(p_xpaths(str(x))["odds"]).get_attribute("innerHTML")
        except:
            odds = 0
        nr[country] = odds


    #push the data to the DB

    cursor.execute("""SELECT *
                            FROM ODDS_DATA
                            ORDER BY id DESC
                            LIMIT 1"""
                            )
    try:
        new_id = cursor.fetchall()[0][0] + 1
    except IndexError:
        new_id = 1

    now = datetime.datetime.now()
    insert = f""" INSERT INTO ODDS_DATA(id,time,FRANCE,GERMANY,ENGLAND,BELGIUM,SPAIN,ITALY,PORTUGAL,
                    NETHERLANDS,CROATIA,SWITZERLAND,DENMARK,UKRAINE,SWEDEN,AUSTRIA,POLAND,TURKEY,CZECH_REPUBLIC,
                    WALES,SCOTLAND,RUSSIA,FINLAND,NORTH_MACEDONIA,HUNGARY,SLOVAKIA) 
                    VALUES({new_id},'{str(now)}','{nr["FRANCE"]}','{nr["GERMANY"]}','{nr["ENGLAND"]}','{nr["BELGIUM"]}',
                    '{nr["SPAIN"]}','{nr["ITALY"]}','{nr["PORTUGAL"]}','{nr["NETHERLANDS"]}','{nr["CROATIA"]}','{nr["SWITZERLAND"]}',
                    '{nr["DENMARK"]}','{nr["UKRAINE"]}','{nr["SWEDEN"]}','{nr["AUSTRIA"]}','{nr["POLAND"]}','{nr["TURKEY"]}','{nr["CZECH_REPUBLIC"]}',
                    '{nr["WALES"]}','{nr["SCOTLAND"]}','{nr["RUSSIA"]}','{nr["FINLAND"]}','{nr["NORTH_MACEDONIA"]}','{nr["HUNGARY"]}','{nr["SLOVAKIA"]}'
    )"""


    cursor.execute(insert)
    connection.commit()
    print("wrote data to DB")
    
    driver.refresh()



cursor.close()


time.sleep(10)
driver.close()




time.sleep(10)
