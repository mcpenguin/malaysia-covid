import datetime
import requests
import string
from bs4 import BeautifulSoup

# Malay month list
month_list = [
    'januari',
    'februari',
    'mac',
    'april',
    'mei',
    'jun',
    'julai',
    'ogos',
    'september',
    'oktober',
    'november',
    'disember'
]

# convert datetime.date object into "DD-MMM-YYYY", where MMM is a Malay month
def convertDate(date):
    return date.strftime("%#d-{}-%Y".format(month_list[int(date.strftime("%m"))-1]))


# initialize parameter value to name mapping
vtt_map = {
    'cured_cases': 'Kes sembuh',
    'new_cases': 'Kes baharu',
    'import_cases': 'Kes import',
    'local_cases': 'Kes tempatan',
    'active_cases': 'Kes aktif',
    'resp_asst_cases': 'Kes yang memerlukan rawatan',
    'death_cases': 'Kes kematian',
    # 'number_of_clusters': 'Jumlah kluster',
    # 'number_of_new_clusters': 'Jumlah kluster baharu',
    # 'number_of_expired_clusters': 'Jumlah kluster yang telah tamat',
    # 'number_of_active_clusters': 'Jumlah kluster aktif'
}

# make url of blog post using date object
def makeURL(date):
    return "https://kpkesihatan.com/{}/kenyataan-akhbar-kpk-{}-situasi-semasa-jangkitan-penyakit-coronavirus-2019-covid-19-di-malaysia/".format(
        date.strftime("%#d/%#m/%Y"),
        convertDate(date)
    )

# function to get data from website by date
def get_data(date):
    # make url to website for date
    url = makeURL(date)
    result = None
    response = None

    # get content of website
    response = requests.get(url)

    if (response.status_code == 200):
        # filter for the case data
        # create soup object
        soup = BeautifulSoup(response.content, 'html.parser')
        # get all bulleted lists
        result = soup.find_all('ul')
        cases_content = str(result[1])

        # get soup for cases
        soup_cases = BeautifulSoup(cases_content, 'html.parser')

        # initialize date in result object
        day_data = {'date': date.strftime("%d/%m/%Y")}

        # store the data into the result object
        for var in vtt_map:
            # Get the string containing the key words
            keyword_string = str(soup_cases.find(
                lambda tag: tag.name == "li" and vtt_map[var] in tag.text))
            # Get the soup for the specific string
            soup_var = BeautifulSoup(keyword_string, 'html.parser')
            # use the custom soup to extract the case data, which is stored in strong tags
            strongs = list(soup_var.findAll(
                lambda tag: tag.name == "strong"))
            # sometimes, there may be *two* strong tags together, so we
            # have to join the contents of the strong tags to get the final value
            content = "".join(j for i in map(lambda s: s.contents, strongs) for j in i)
            # parse the content to only extract the integer part for the corresponding variable
            for s in ["\xa0", "kes", "kluster", " ", ",", ";"]:
                content = content.replace(s, "")
            # convert the integer part to an int
            day_data[var] = int(content)

        # return result when done
        return day_data
    else:
        print("{} returned {} error".format(url, response.status_code))
        return {}
