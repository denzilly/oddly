import platform
import os
import pyarrow as pa
import redis
import pandas as pd

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
