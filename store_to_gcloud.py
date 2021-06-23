import mysql.connector as msc
import json
import pandas as pd
import numpy as np
import datetime

from fetch_data import get_data

# read config file into JSON object
configFile = open('config.json')
config = json.load(configFile)

# make connection to the GCloud database
db_config = config['database']
connection = msc.connect(
    host=db_config['host'], 
    port=db_config['port'],
    user=db_config['user'],
    password=db_config['password'],
    database=db_config['database']
)
cursor = connection.cursor()

# import csv data into database
# df = pd.read_csv("covid_data.csv")
# store data from today into database
df = pd.DataFrame([get_data(datetime.date.today())])

# store dataframe into sql db
for row in df.values:
    # get values to be inserted

    # vals = tuple(np.delete(row, 0)) # use this line if importing csv data into db
    vals = tuple(row) # use this line if storing data from today into db

    # make sql query
    sql = "INSERT INTO malaysia_covid_data VALUES (STR_TO_DATE(%s, '%d/%m/%Y'), %s, %s, %s, %s, %s, %s, %s)"
    # execute and commit query
    cursor.execute(sql, vals)
    connection.commit()