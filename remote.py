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
    time.sleep(3)

    market = driver.find_element_by_xpath(\
                    b_xpaths(str(country_coords()[country][0]),\
                    str(country_coords()[country][1]))["market"]).get_attribute("innerHTML").upper()  
                          
    if market == country:
        if direction == "buy":

            driver.find_element_by_xpath(\
                    b_xpaths(str(country_coords()[country][0]),\
                    str(country_coords()[country][1]))["offer"]).click()

        elif direction == "sell":
            driver.find_element_by_xpath(\
                    b_xpaths(str(country_coords()[country][0]),\
                    str(country_coords()[country][1]))["bid"]).click()



trade(driver, "sell","WALES")