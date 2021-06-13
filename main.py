import pystore
import os
import pandas


db_path = os.getcwd() + "\\data"
pystore.set_path(db_path)

store = pystore.store('odds_data')
pystore.list_stores()



