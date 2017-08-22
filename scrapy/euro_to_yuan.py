import urllib2
import csv
import time
from datetime import datetime
from bs4 import BeautifulSoup

page = 'http://www.xe.com/fr/currencyconverter/convert/?Amount=1&From=EUR&To=CNY'

with open('index.csv','a') as csv_file:
    writer = csv.writer(csv_file)
    for i in range(20):
        pg = urllib2.urlopen(page)

        soup = BeautifulSoup(pg,'html.parser')
        price_box = soup.find('span',attrs={'class':'uccResultAmount'})
        price = price_box.text
        writer.writerow([price,datetime.now()])
        time.sleep(10)