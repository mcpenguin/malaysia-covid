# Malaysian COVID-19 data

The purpose of this project is to automatically fetch Malaysian COVID-19 data from MOH's tweets 
(@KKMPutrajaya) and stores them in a central database, which can then be queried for data analysis.

## Process
- The data is first extracted by using the Twitter API as a list of tweets, querying for tweets with the key words
"Status Terkini #COVID19".
- Then, the data is parsed to extract the relevant COVID-19 case data.
- The data is then stored into a Google Cloud MySQL database (not implemented yet).

## Notes
- Since the Twitter account was only created in early March, COVID-19 case data is only available
from early March onwards.
