
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



#connect to the database
connection = db_connect("odds_DB")
cursor = connection.cursor()



options=Options()
options.headless = True


driver = webdriver.Firefox(options=options,executable_path=identify_os())
driver.get("https://www.paddypower.com/football/uefa-euro-2020?tab=outrights")
driver.set_window_size(1440, 900)

time.sleep(3)
try:
    #sometimes the cookie thing just doesn't show up
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, p_xpaths("none")["cookies"]))).click()
except:
	pass

try:
    while True:
        
        time.sleep(1)
        
        #driver.execute_script("return arguments[0].scrollIntoView();", driver.find_element_by_xpath(p_xpaths("none")["showall"]))
        time.sleep(1)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, p_xpaths("none")["showall"]))).click()
        



        nr = {time : datetime.datetime.now()}
        for x in range(1,25):
            country = driver.find_element_by_xpath(p_xpaths(str(x))["country"]).get_attribute("innerHTML").upper().replace(" ","_")
            try:
                odds = float(eval(driver.find_element_by_xpath(p_xpaths(str(x))["odds"]).get_attribute("innerHTML")))
            except:
                odds = 0
            nr[country] = odds

        values = [value for key,value in nr.items()][1:]



        #push the data to the DB
        if  sum(values) != 0:
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
            time.sleep(10)
            
except Exception as e:
    print(e)
    print("script failed due to error, will restart in 10 seconds") 
    
    


#close cursors and browser in case of error
cursor.close()
connection.close()
driver.close()
time.sleep(5)