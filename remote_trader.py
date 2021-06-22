from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
from configparser import ConfigParser

from xpaths import *
from modules.helpers import *
import keyboard
import time
import os

config = ConfigParser()
config.read(f'{os.getcwd()}/modules/config.ini')


options=Options()
options.headless = False


driver = webdriver.Firefox(options=options,executable_path=identify_os())
driver.get("http://www.betmkt.com/login.html")
#driver.get(f'{os.getcwd()}betmkt.html')

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, b_xpaths("n","n")["email"]))).send_keys(config.get('main','buser'))
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, b_xpaths("n","n")["password"]))).send_keys(config.get('main','bpass'))
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, b_xpaths("n","n")["password"]))).send_keys(Keys.RETURN)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, b_xpaths("1","1")["market"])))
time.sleep(3)

print("trader ready")



def trade(driver, direction, country):
    time.sleep(0.1)

    market = driver.find_element_by_xpath(\
                    b_xpaths(str(country_coords()[country][0]),\
                    str(country_coords()[country][1]))["market"]).get_attribute("innerHTML").upper()  
                          
    if market == country:

        driver.find_element_by_xpath(\
                    b_xpaths(str(country_coords()[country][0]),\
                    str(country_coords()[country][1]))["offer"]).click()
        if direction == "buy":
            try:
                print(f"BUYING {country}")
                
                #LIVE CODE DO NOT UNCOMMENT
                # driver.find_element_by_xpath(\
                #     b_xpaths(str(country_coords()[country][0]),\
                #     str(country_coords()[country][1]))["buy"]).click()
            except:
                print("unable to buy")                   

        elif direction == "sell":
            try:
                print(f"SELLING {country}")
                #LIVE CODE DO NOT UNCOMMENT
                # driver.find_element_by_xpath(\
                #     b_xpaths(str(country_coords()[country][0]),\
                #     str(country_coords()[country][1]))["sell"]).click()
            except:
                print("unable to buy")                   


    time.sleep(0.1)
    try:
        driver.find_element_by_xpath(\
                    b_xpaths(str(country_coords()[country][0]),\
                    str(country_coords()[country][1]))["close"]).click()
    except:
        print("trade successful")





buyc1 = "shift + ctrl + 2"
sellc1 = "shift + ctrl + 1"

buyc2 = "shift + ctrl + 4"
sellc2 = "shift + ctrl + 3"

country1 = "WALES"
country2 = "FINLAND"


while True:
    if keyboard.is_pressed(buyc1):
        print("buyc1")
        trade(driver, "buy",country1)
        time.sleep(0.5)
    elif keyboard.is_pressed(sellc1):
        print("sellc1")
        trade(driver, "sell",country1)
        time.sleep(0.5)
    elif keyboard.is_pressed(buyc2):
        print("buyc2")
        trade(driver, "buy",country2)
        time.sleep(0.5)
    elif keyboard.is_pressed(sellc2):
        print("sellc2")
        trade(driver, "sell",country2)
        time.sleep(0.5)
  
    time.sleep(.01)




    