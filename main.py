import pandas as pd
import mysql.connector as msc
import json

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

print(connection);