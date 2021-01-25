import sys, os, re
import logging
import requests
from bs4 import BeautifulSoup
import json
import pathlib

class Scrapper:
    
    def get_current_path(self):
        return str(pathlib.Path(__file__).parent.absolute())
        
    def get_urL(self, pattern):
        file_data = self.read('websites.txt')
        file_url = re.search(pattern, file_data).group(1).strip()
        return file_url
        
    def read(self, file):
        try:
            with open(self.get_current_path() + '\\' + file,'r') as f:
                return f.read()
        except:
            return None   
        
    def write(self, file, data):
        try:
            with open(self.get_current_path() + '\\' + file, 'w') as f:
                return f.write(data)
        except:
            return None   
        
    def get(self, url): 
        return requests.get(url)
        
    def initBS(self, data):
        return BeautifulSoup(data.text, 'html.parser')
    
    def table_scrapper(self, soup, table_attr_type, table_attr_name):
        leaderboard_table = soup.find('table', { table_attr_type: table_attr_name })
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
                
        return table_data
        
    def json_converter(self, table_list):
        return json.dumps(table_data, indent=4)   
     
scrapper = Scrapper()
umg_url = scrapper.get_urL('(?<=UGM:)(.*)')
umg_data = scrapper.get(umg_url)
soup = scrapper.initBS(umg_data)
table_data = scrapper.table_scrapper(soup, 'id', 'leaderboard-table')
json_data = scrapper.json_converter(table_data)
scrapper.write('extracted_data.json', json_data)