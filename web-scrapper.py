import sys, os, re
import logging
import requests
from bs4 import BeautifulSoup
import json

nba_url = 'https://umggaming.com/leaderboards'

data = requests.get(nba_url)

soup = BeautifulSoup(data.text, 'html.parser')

leaderboard_table = soup.find('table', id='leaderboard-table')

table_data = []
fields = []

for tr in leaderboard_table.find_all('tr'):
    for th in tr.find_all('th'):
        fields.append(th.text)
        
for tr in leaderboard_table.find_all('tr'):
    datum = {}
    for i, td in enumerate(tr.find_all('td')):
        datum[fields[i]] = ' '.join(td.text.split())
    if datum:
        table_data.append(datum)
        
json_data = json.dumps(table_data, indent=4)   

# with open('C:\\Users\\danih\\Desktop\\web-scrapper\\json_data.json', 'w') as arquivo:
#     arquivo.write(json_data)