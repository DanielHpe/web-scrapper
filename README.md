PYTHON APPLICATION

- Fetch data from several tables (rankings, leaderboards and etc) | URLs: websites.txt
- Retrieves data such as ranking, team, trophees and orders
- Scrapper Class reads URLs from websites.txt using REGEX
- Add website in file with " " separation and just pass the attributes to script
- file "script_list" contains some examples
- Pass the URL_KEY in "websites.txt", the html element type (id, class, name) and the html value
- The SCRAPPER parses only table elements to demonstration
- The script generates a "extratec_data.json" file with the data retrieved converted in json
- Use of library such as beautiful soup to html parsing and request to http requests
