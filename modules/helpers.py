import platform
import os
import pyarrow as pa
import redis
import pandas as pd
import dash_core_components as dcc
import dateutil
import re
import datetime

def identify_os():

    if "windows" in platform.system().lower():
        path = f"{os.getcwd()}\\resources\\geckodriver.exe"
    elif "linux" in platform.system().lower():
        path = f"resources/geckodriver"
        print(path)
    else:
        print("unknown os")
    return path


print(identify_os())


def storeInRedis(r, alias, df):
    df_compressed = pa.serialize(df).to_buffer().to_pybytes()
    res = r.set(alias,df_compressed)
    if res == True:
        print(f'{alias} cached')

def loadFromRedis(r, alias):
    data = r.get(alias)
    try:
        return pa.deserialize(data)
    except:
        return pd.DataFrame({'A' : []})


def price_string(df, country, bo):
    if bo == "bid":
        temp  = df[f"{country}_BID"].iloc[-1]
        return f"SELL @ {temp}"
        

    elif bo == "offer":
        temp  = df[f"{country}_OFFER"].iloc[-1]
        return f"BUY @ {temp}"
    

def country_code(country):
    country_mapping = {"BELGIUM":"BEL",
                        "ITALY":"ITA",
                        "RUSSIA":"RUS",
                        "POLAND":"POL",
                        "UKRAINE":"UKR",
                        "SPAIN":"SPA",
                        "FRANCE":"FRA",
                        "TURKEY":"TUR",
                        "ENGLAND":"ENG",
                        "CZECH_REPUBLIC":"CZK",
                        "FINLAND":"FIN",
                        "SWEDEN":"SWE",
                        "CROATIA":"CRO",
                        "AUSTRIA":"AUT",
                        "NETHERLANDS":"NED",
                        "GERMANY":"GER",
                        "PORTUGAL":"POR",
                        "SWITZERLAND":"SWI",
                        "DENMARK":"DEN",
                        "WALES":"WAL",
                        "NORTH_MACEDONIA":"NOM",
                        "HUNGARY":"HUN",
                        "SLOVAKIA":"SLO",
                        "SCOTLAND":"SCO",}


    return country_mapping[country]





    
