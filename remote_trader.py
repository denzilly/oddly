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

debug_mode = False

if debug_mode == True:
    print("LAUNCHING IN DEBUG MDOE")
else:
    print("*************LAUNCHING IN LIVE TRADING MODE*********")

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

                if debug_mode == False:
                    #LIVE CODE DO NOT UNCOMMENT
                    driver.find_element_by_xpath(\
                        b_xpaths(str(country_coords()[country][0]),\
                        str(country_coords()[country][1]))["buy"]).click()
                    print("actually trading")

            except:
                print("unable to buy")                   

        elif direction == "sell":
            try:
                print(f"SELLING {country}")
                if debug_mode == False:
                    
                    #LIVE CODE DO NOT UNCOMMENT
                    driver.find_element_by_xpath(\
                        b_xpaths(str(country_coords()[country][0]),\
                        str(country_coords()[country][1]))["sell"]).click()

                    print("actually trading")
            except:
                print("unable to sell")                   


    time.sleep(0.1)
    try:
        time.sleep(0.3)
        driver.find_element_by_xpath(\
                    b_xpaths(str(country_coords()[country][0]),\
                    str(country_coords()[country][1]))["close"]).click()
    except:
        print("trade successful")





#hotkey logic


country1 = "ITALY"
country2 = "AUSTRIA"

c1_sell = "F19"
c1_buy = "F20"
c2_sell = "F16"
c2_buy = "F17"
arm = "F24"
armed = False

print(f"COUNTRY 1:{country1}")
print(f"COUNTRY 2:{country2}")
while True:

  if keyboard.is_pressed(arm):
      if armed == False:
        print("ARMED!")
        armed = True
        time.sleep(0.2)
      else:
        print("DISARMED!")
        armed = False
        time.sleep(0.2)

  if armed == True:
    if keyboard.is_pressed(c1_sell):
      trade(driver, "sell", country1)
      time.sleep(0.2)
    elif keyboard.is_pressed(c1_buy):
      trade(driver, "buy", country1)
      time.sleep(0.2)
    elif keyboard.is_pressed(c2_sell):
      trade(driver, "sell", country2)
      time.sleep(0.2)
    elif keyboard.is_pressed(c2_buy):
      trade(driver, "buy", country2)
      time.sleep(0.2)
  
  time.sleep(0.01)




    