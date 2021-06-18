import os
import pandas
import time
import datetime
from configparser import ConfigParser



from xpaths import *
from modules.helpers import *
from modules.db_logic import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys



#connect to the database
connection = db_connect("market_DB")
cursor = connection.cursor()



#read config
config = ConfigParser()
config.read(f'{os.getcwd()}/modules/config.ini')

options=Options()
options.headless = True


driver = webdriver.Firefox(options=options,executable_path=identify_os())
driver.get("http://www.betmkt.com/login.html")



    
time.sleep(3)
    

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, b_xpaths("n","n")["email"]))).send_keys(config.get('main','buser'))
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, b_xpaths("n","n")["password"]))).send_keys(config.get('main','bpass'))
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, b_xpaths("n","n")["password"]))).send_keys(Keys.RETURN)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, b_xpaths("1","1")["market"])))


while True:
    nr = {"time" : datetime.datetime.now()}
    count = 1
    for x in [6,4,4,4,4,4,4,6,3]:
        for row in range(1,x+1):
            market = driver.find_element_by_xpath(b_xpaths(str(count), str(row))["market"]).get_attribute("innerHTML").upper().replace(" ","_").replace("@","")
            nr[market +"_BID"] = driver.find_element_by_xpath(b_xpaths(str(count), str(row))["bid"]).get_attribute("innerHTML")
            nr[market +"_OFFER"] = driver.find_element_by_xpath(b_xpaths(str(count), str(row))["offer"]).get_attribute("innerHTML")
        count += 1


    print(nr)
    #push the data to the DB

    cursor.execute("""SELECT *
                                FROM MARKET_DATA
                                ORDER BY id DESC
                                LIMIT 1"""
                                )
    try:
        new_id = cursor.fetchall()[0][0] + 1
    except IndexError:
        new_id = 1


    now = datetime.datetime.now()
    
    cursor.execute(m_insert_q(nr,new_id,now))
    connection.commit()
    print("wrote data to DB")
    time.sleep(5)
    



cursor.close()


time.sleep(10)
driver.close()




time.sleep(10)
