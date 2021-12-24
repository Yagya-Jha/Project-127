import pandas as pd
from selenium import webdriver as wd
from bs4 import BeautifulSoup as bs
import time
import csv

START_URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = wd.Chrome("./chromedriver/chromedriver.exe")

browser.get(START_URL)
time.sleep(10)

header = ["Name", "Distance", "Mass", "Radius"]
star_data = []

def scraep():

    # for i in range(0,100):
    soup = bs(browser.page_source, "html.parser")
    for table_tag in soup.find_all("table", attrs={"class", "wikitable sortable jquery-tablesorter"}):
        tr_tag = table_tag.find_all("tr")
        temp_list = []
        for index, tr in enumerate(tr_tag):
            # print(index)
            td=tr.find_all("td")
            row=[i.text.rstrip() for i in td]
            temp_list.append(row)
                # if index==0:
                #     print('\n _______________________debug code begins_____________________')
                #     print(tr.find_all("td"))

                #     temp_list.append(tr.find_all("td")[0].contents[0])
                # else:
                #     try:
                #         temp_list.append(tr.contents[0])
                #     except:
                #         temp_list.append("")

        star_data.append(temp_list)
        # print(star_data)
            # print("This is temp_list \/")
            # print(temp_list)

    name = []
    distance = []
    mass = []
    radius = []

    for i in range(1, len(temp_list)):
        name.append(temp_list[i][1])
        distance.append(temp_list[i][3])
        mass.append(temp_list[i][5])
        radius.append(temp_list[i][6])

    df = pd.DataFrame(list(zip(name, distance, mass, radius)), columns=header)
    df.to_csv('scrapper.csv')

scraep()
