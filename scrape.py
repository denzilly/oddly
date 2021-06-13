from bs4 import BeautifulSoup
from lxml import etree
from xpaths import *
import requests
import statistics




def  get_soup():

    url = "https://www.oddschecker.com/football/euro-2020/winner"
    page = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})

    soup = BeautifulSoup(page.content,'html.parser')

    dom = etree.HTML(str(soup))

    return dom




def scrape_odds(row, dom):

    
    #print(soup)
    c_name = dom.xpath(get_xpaths(row)[0])[0].text
    print(c_name)
    odds = [] 
    for x in range (1,11):
        try:
            odds.append(eval(dom.xpath(get_xpaths(row)[x])[0].text))
        except IndexError:
            pass
    m_odds = statistics.median(odds)
    print(f"median odds are:{m_odds}")






dom = get_soup()

for x in range(1,25):
    scrape_odds(str(x),dom)
