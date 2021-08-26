# %% [markdown]
# # Fetching data from COVID19.place
# 
# url used: https://covid19.place/MY/en-US
# updated every day

# %%
# import necessary libraries
from datetime import date
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv('MONGO_URL')
client = MongoClient(MONGO_URL)


# %%
url = "https://covid19.place/MY/en-US"


# %%
# get content of website
response = requests.get(url)
# create soup object to parse website
soup_general = bs(response.content, 'html.parser')
# %%
# get new cases by area/city
area_stats = soup_general.find_all("section", {"id": "area"})

# %%
# list of states
stateList = ['selangor', 'kualalumpur', 'putrajaya', 'ppinang', 'johor', 'nsembilan', 'pahang', 'kelantan',
'kedah', 'perak', 'melaka', 'terengganu', 'perlis', 'sabah', 'labuan', 'sarawak']


# %%
# find all tables in area section
area_soup = bs(str(area_stats), 'html.parser')
tableList = area_soup.find_all("table")

# %% [markdown]
# ### We make a helper function to help us extract data from a specific state.

# %%
def fetch_state_data(state_id):

    # get the unparsed data first
    state_soup = state_soups[state_id]
    unparsed_data = state_soup.find("tbody").contents

    # initialize result set
    # which is a dict with keys = district, and element = lists of lists of [name, new, 14 days, active, total]
    result = []

    # initialize local bucket list
    # l = []
    # var to hold current district name
    district_name = 'misc'
    # get the relevant data
    for table_row in unparsed_data:
        # if its a data row
        if table_row.contents[0].name == 'td':
            # then add its contents to l
            result += [
                {
                    'state': state_id,
                    'district_name': district_name,
                    'area_name': table_row.contents[0].text,
                    'new': table_row.contents[1].text,
                    '14_days': table_row.contents[2].text,
                    'active': table_row.contents[3].text,
                    'total': table_row.contents[4].text,
                    'date': date.today().strftime("%Y-%m-%d")
                }
            ]
        # otherwise, its a new district, so we reset the local "district-specific"
        # list and move on to the next district
        else:
            # result[district_name] = l
            # # reset vars
            # l = []
            district_name = table_row.contents[0].text

    # add the last district to the result
    # result[district_name] = l
    try:
        result += [
            {
                'state': state_id,
                'district_name': district_name,
                'area_name': table_row.contents[0].text,
                'new': table_row.contents[1].text,
                '14_days': table_row.contents[2].text,
                'active': table_row.contents[3].text,
                'total': table_row.contents[4].text,
                'date': date.today().strftime("%Y-%m-%d")
            }
        ]
    except Exception as e:
        pass # ignore if still update in progress

    # return the result
    return result

# Since we have established that this method successfully fetches data for each state, we can
# now repeat the same process for every state.

# %%

# python function to flatten list of lists
def flatten(l):
    return [item for sublist in l for item in sublist]

# make dict for state soups
state_soups = {stateList[i]: bs(str(tableList[i]), 'html.parser') for i in range(len(stateList))}
data = flatten([fetch_state_data(state_id) for state_id in stateList])

# insert data into database
client['msiacovid']['malaysia_covid_area_cases'].insert_many(data)



