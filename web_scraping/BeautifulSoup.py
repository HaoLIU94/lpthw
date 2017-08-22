import urllib2
import csv
import time
from datetime import datetime
from bs4 import BeautifulSoup

quote_page = ['http://www.bloomberg.com/quote/SPX:IND',
            'http://www.bloomberg.com/quote/CCMP:IND']

data = []
for i in range(5):
    for pg in quote_page:
        page = urllib2.urlopen(pg)

        soup = BeautifulSoup(page,'html.parser')
        name_box = soup.find('div',attrs={'class':'ticker'})
        name = name_box.text.strip()

        price_box = soup.find('div',attrs={'class':'price'})
        price = price_box.text

        data.append((name,price))
        time.sleep(1)

with open('index.csv','a') as csv_file:
    writer = csv.writer(csv_file)
    for name,price in data:
        writer.writerow([name,price,datetime.now()])