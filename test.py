import pystore
import os

import pandas as pd


cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
        'Price': [22000,25000,27000,35000]
        }

df = pd.DataFrame(cars, columns = ['Brand', 'Price'])




db_path = os.getcwd() + "\\data"
pystore.set_path(db_path)

store = pystore.store('test_data')
collection = store.collection("coll1")

store.list_collections()
