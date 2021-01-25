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
        try:
            status_code = requests.get(url).status_code
            if status_code == 200:
                return requests.get(url)
            return None
        except:
            return None
        
    def init_BS(self, data):
        return BeautifulSoup(data.text, 'html.parser')
    
    def table_scrapper(self, soup, table_attr_type, table_attr_name):
        leaderboard_table = soup.find('table', { table_attr_type: table_attr_name })  

        table_data = []
        fields = []
        
        if leaderboard_table is not None:
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
        
        table_data.append({'message':'NAO FOI POSSIVEL REALIZAR SCRAPPING DA TABELA PASSADA'})
        return table_data
        
    def json_converter(self, table_list):
        return json.dumps(table_list, indent=4)   
     
scrapper = Scrapper()
table_data = []

url_ref = sys.argv[1]

if url_ref not in scrapper.read('websites.txt'):
    table_data.append({'message': 'NENHUM ARGUMENTO PASSADO DE UMA URL VALIDA DE "WEBSITES.TXT"'})
    json_data = scrapper.json_converter(table_data)
    scrapper.write('extracted_data.json', json_data)
    exit()

url = scrapper.get_urL(f'(?<={url_ref})(.*)')
get_data = scrapper.get(url)

if get_data is not None:   
    soup = scrapper.init_BS(get_data)
    html_element = sys.argv[2]
    html_value = sys.argv[3]
    table_data =  scrapper.table_scrapper(soup, html_element, html_value)
    json_data = scrapper.json_converter(table_data)
    scrapper.write('extracted_data.json', json_data)
    exit()
    
table_data.append({'message': 'URL INVÁLIDA OU STATUS CODE DO REQUEST DIFERENTE DE 200 (SUCESSO)'})
json_data = scrapper.json_converter(table_data)
scrapper.write('extracted_data.json', json_data)