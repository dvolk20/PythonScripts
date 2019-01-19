import requests
import csv
from bs4 import BeautifulSoup

url = "http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html"

page = requests.get(url)

#print(page) #this will print the status 

page_html = page.content #gets all of the page html

soup = BeautifulSoup(page_html, 'html.parser')

a = soup.prettify() #this is the 'pretty' version of the html
b = soup.find_all('p') #this finds all items in the p tag
c = soup.find_all(class_="outer-text") #finds based on class
d = soup.find_all(id="first") #finds based on id

for item in b:
    print(item.get_text())

#print(b)
