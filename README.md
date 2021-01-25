PYTHON APPLICATION TO FETCH DATA FROM WEBSITES

- Fetch data from several tables (rankings, leaderboards and etc) | URLs: websites.txt
- Retrieves data such as ranking, team, trophees, points, phone codes and orders
- Scrapper Class reads URLs from websites.txt using REGEX
- file "script_list" contains list of args
- The "web-scrapper.py" loops the "script_list.txt" using each line as a diferent website from "websites.txt"
- Just add more info in "websites.txt" and "script_list.txt" to retrieve more data from diferent datasets
- The SCRAPPER parses only table elements to demonstration
- Use of library such as beautiful soup to html parsing and request to http requests
- RUN: To run the app, just run the "run_scrapper.bat" as admin (WINDOWS)
- TESTS: Execution time with 5 sites: 20s (4s to scrap each site as average)