import pandas as pd
import mysql.connector as msc
import datetime
from dateutil.rrule import rrule, DAILY
import json

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

# fetch all data from Jan 20 to now
def fetch_all_data():
    # insert data from Jan onwards into dataset
    dataset = []
    start_date = datetime.date(2021, 1, 20)
    end_date = datetime.date.today()

    for dt in rrule(DAILY, dtstart=start_date, until=end_date):
        try:
            dataset.append(get_data(dt))
            print("Data retrieved for the date {}".format(dt.strftime("%d/%m/%Y")))
        except:
            print("Unable to retrieve data for the date {}".format(dt.strftime("%d/%m/%Y")))

    return dataset

# fetch all data and store in dataframe
df = pd.DataFrame(fetch_all_data())
# put dataframe to csv
df.to_csv("covid_data.csv")
