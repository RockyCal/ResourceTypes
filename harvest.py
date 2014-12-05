__author__ = 'Raquel'

from bs4 import BeautifulSoup
from urllib.request import urlopen
from pymongo import MongoClient, errors

client = MongoClient()

db = client.resourceTypes
types = db.types

soup = BeautifulSoup(urlopen('http://neurolex.org/wiki/Category:Resource:CINERGI').read())
table = soup.find('table', {'class': "smwtable", 'id': "querytable21"})
rows = table.find_all('tr')
rows.pop(0)
for row in rows:
    tds = row.find_all('td')
    url = ''
    if tds[2].find('a'):
        if tds[2].find('a').has_attr('href'):
            url = tds[2].find('a')['href']
    new_type = {'_id': tds[3].text, 'name': tds[0].text, 'URL': url, 'SuperCategory:': tds[1].text}
    try:
        new_type_id = types.insert(new_type)
    except errors.DuplicateKeyError:
        continue
    print(new_type_id)
