#Script to get all urls from a webpage 

from bs4 import BeautifulSoup, SoupStrainer
import requests

url = 'http://python.org/'

page = requests.get(url)
data = page.text
soup = BeautifulSoup(data)

#print(soup)

for link in soup.find_all('a'):
    print(link.get('href'))