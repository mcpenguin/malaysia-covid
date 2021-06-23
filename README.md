# Malaysian COVID-19 data (from 20/1/2021 onwards)

The purpose of this project is to automatically fetch Malaysian COVID-19 data from https://kpkesihatan.com/ and stores them in a CSV, 
which can then be used for data analysis.

## Testing

Simply clone this repository and run ```python main.py``` in the command prompt.

## Process
- The data is first extracted by using the BeautifulSoup library to
scrape the HTML content from each day's blog page.
- Then, the content is parsed to extract the relevant COVID-19 data.
- The data is then stored into a CSV, ```covid-data.csv```, for public use.

## Plans
- Migrate data to Google Cloud database
- Create task scheduler on laptop to automatically fetch data every day (the
top task makes this step much easier)
- Create a dashboard using Django (or another Python web development tool)

## Notes
- If you see the ```testing.ipynb``` document, which I used to as a testing
playground, you will notice I initially tried to query
the data using the **Twitter API**. However, since you can only query the most recent
3200 tweets, this is not feasible as a data extraction method.
- Prior to 20 January 2021, the posts on the website are in paragraph form, making it
exponentially harder to parse the data into case data without doing it manually. 
In the future, it might be possible to utilize NLP algorithms to parse the data.
- In the current dataset, some dates are missing, as their pages did not "fit" the
template generally used in the posts. For these dates, the data must be inputted manually.
