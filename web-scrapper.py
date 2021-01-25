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
        file_data = self.read(self.get_current_path(), 'websites.txt')
        file_url = re.search(pattern, file_data).group(1).strip()
        return file_url
        
    def read(self, folder, file):
        if not os.path.exists(folder):
            os.makedirs(folder)
        try:
            with open(folder + '\\' + file,'r') as f:
                return f.read()
        except:
            return None   
        
    def write(self, folder, file, data):
        if not os.path.exists(folder):
            os.makedirs(folder)
        try:
            with open(folder + '\\' + file, 'w') as f:
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
                    fields.append(' '.join(th.text.split()))

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

scripts_text = scrapper.read(scrapper.get_current_path(), 'script_list.txt')

for line in scripts_text.split('\n'):
    script_line = re.search(r'(?<=\[)(.*)(?=])', line).group(1).strip()
    script_ref = script_line.split(" ")[0].strip()
    script_name = script_line.split(" ")[1].strip()
    script_key = script_line.split(" ")[2].strip()
    script_element = script_line.split(" ")[3].strip()
    script_value = script_line.split(" ")[4].strip()
    output_file = f'extracted_data_{script_key}.json'
    
    url = scrapper.get_urL(f'(?<={script_key})(.*)')
    get_data = scrapper.get(url)

    if get_data is not None:   
        soup = scrapper.init_BS(get_data)
        table_data =  scrapper.table_scrapper(soup, script_element, script_value)
        json_data = scrapper.json_converter(table_data)
        scrapper.write(scrapper.get_current_path() + '\\outputs', output_file, json_data)
    else:
        table_data.append({'message': 'URL INVÁLIDA OU STATUS CODE DO REQUEST DIFERENTE DE 200 (SUCESSO)'})
        json_data = scrapper.json_converter(table_data)
        scrapper.write(scrapper.get_current_path() + '\\outputs', output_file, json_data)