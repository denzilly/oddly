import pystore
import os
import pandas
import time

from xpaths import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
driver.get("https://www.paddypower.com/football/uefa-euro-2020?tab=outrights")

driver.execute_script("window.scrollTo(0, 500)")

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, p_xpaths("none")["showall"]))).click()
time.sleep(1)
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, p_xpaths("none")["cookies"]))).click()


for x in range(1,25):
    print(driver.find_element_by_xpath(p_xpaths(str(x))["country"]).get_attribute("innerHTML"))
    print(driver.find_element_by_xpath(p_xpaths(str(x))["odds"]).get_attribute("innerHTML"))



time.sleep(10)
driver.close()


db_path = os.getcwd() + "\\data"
pystore.set_path(db_path)

store = pystore.store('odds_data')
pystore.list_stores()


time.sleep(10)
