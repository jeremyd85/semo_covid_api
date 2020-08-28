from bs4 import BeautifulSoup
import csv
import requests
from datetime import datetime


semo_url = 'https://semo.edu/sealerts/covid19/daily-cases.html'

def write_rows(filename, rows):
    with open(filename, 'w+') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


def scrape_info():
    covid_cases = []
    response = requests.get(semo_url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    table_rows = soup.find_all('tr')
    for tr in table_rows:
        tds = tr.find_all('td')
        if tds:
            case_day = {
                'date': tds[0].find('strong').text,
                'employee_cases': tds[1].text,
                'student_cases': tds[2].text
            }
            if case_day['date'] != 'TOTAL':
                covid_cases.append(case_day)
    write_rows('semo_cases.csv', covid_cases)
        
if __name__ == '__main__':
    scrape_info()