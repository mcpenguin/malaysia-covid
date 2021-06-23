# Malaysian COVID-19 data

The purpose of this project is to automatically fetch Malaysian COVID-19 data from https://kpkesihatan.com/ and stores them in a CSV, 
which can then be used for data analysis.

## Testing

Simply clone this repository and run ```python main.py``` in the command prompt.

## Process
- The data is first extracted by using the BeautifulSoup library to
scrape the HTML content from each day's blog page.
- Then, the content is parsed to extract the relevant COVID-19 data.
- The data is then stored into a CSV for public use.

## Notes
- If you see the ```testing.ipynb``` document, you will notice I initially tried to query
the data using the **Twitter API**. However, since you can only query the most recent
3200 tweets, this is not feasible as a data extraction method.
- Prior to 20 January 2021, the posts on the website are in paragraph form, making it
exponentially harder to parse the data into case data without doing it manually. 
In the future, it might be possible to utilize NLP algorithms to parse the data.
- In the current dataset, some dates are missing, as their pages did not "fit" the
template used in the website. For these dates, the data must be inputted manually.
- There are also some anomalies in the dataset, which must be corrected manually
for similar reasons to the above.
