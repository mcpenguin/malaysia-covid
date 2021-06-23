# fetches all data from 20/01/2021 onwards

import pandas as pd
import mysql.connector as msc
import datetime
from dateutil.rrule import rrule, DAILY
import json

from fetch_data import get_data

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
