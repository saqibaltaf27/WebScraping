import requests
import pandas as pd
import csv
import json
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
          'referer' : 'https://www.zameen.com/Homes/Lahore-1-1.html'
          }

url = 'https://www.zameen.com/Homes/Lahore-1-1.html'
response = requests.get(url = url, headers = headers)
response.status_code
data = BeautifulSoup(response.content, 'html.parser')
listing_1 = data.find_all('ul', class_ = '_357a9937')
#print(listing_1)
list_of_data = []
for listing in listing_1:
    title_1 = listing.find('h1', class_ = '_64bb5b3b')
    if title_1 is not None:
        title = title_1.text.strip()
        title
    
    price_1 = listing.find('div', class_ = 'c4fc20ba')
    if price_1 is not None:
        price = price_1.text.strip()
    price
    
    property_url = listing.find('a', class_ = '_7ac32433') ['href']
    
    list_of_data_1 = {
        'title' : title_1,
        'price' : price_1,
        'link'  : property_url
    }
    
    list_of_data.append(list_of_data_1)
    
for listing in list_of_data:
    print(f"Title : {listing['title']}")
    print(f"Price : {listing['price']}")
    print(f"Url : {listing['link']}")

dataframe = pd.DataFrame.from_dict(list_of_data)
dataframe.to_csv('Properties_data.csv', index = False)
