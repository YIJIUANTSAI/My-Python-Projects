

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def main():
    driver = webdriver.Chrome()
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        driver.get(url)
        try:
            element_present = EC.presence_of_element_located((By.ID, 'specific-element-id'))
            WebDriverWait(driver, 5).until(element_present)
        except TimeoutException:
            print("")
        html = driver.page_source
        soup = BeautifulSoup(html, features="html.parser")
        table = soup.find('table', class_='t-stripe')
        rows = table.find_all('tr')

        male_total = 0
        female_total = 0
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 5:  # ensure complete data (rank, name, male_num, name, female_num)
                male_num = int(cols[2].text.replace(',', ''))
                female_num = int(cols[4].text.replace(',', ''))
                male_total += male_num
                female_total += female_num

        print(f"Male Number: {male_total}")
        print(f"Female Number: {female_total}")


if __name__ == '__main__':
    main()
