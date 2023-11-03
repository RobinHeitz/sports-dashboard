from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import argparse
from bs4 import BeautifulSoup
import re

import datetime
from typing import Tuple

from pydantic import BaseModel

URL = "https://www.liquimoly-hbl.de/de/liqui-moly-hbl/spielplan/saisonen/spielplan/saison-23-24/spielplan-nach-spieltagen/"


class GamePairing(BaseModel):
    gameday: int
    date: datetime.date
    start_time: datetime.time




def main(testing=False):
    
    if testing is True:

        with open("example_html.txt", "r") as f:
            content = f.read()
    else:
        driver = webdriver.Chrome()
        driver.get(URL)
        content = driver.page_source

    soup = BeautifulSoup(content, 'html.parser')
    scheduled_gamedays = soup.find_all('div', class_='schedule')

    for schedule in scheduled_gamedays:
        # print(schedule)
        table = schedule.findChild("table")
        # table.find('thead').find("tr").find("")

        table_header_tag = table.findChild("thead").findChild("tr").findChild("th")
        num_gameday = table_header_tag.string.split(" ")[0].strip().split(".")[0]
        # print(num_gameday)

        table_body = table.findChild("tbody")
        table_rows = table_body.findChildren("tr")

        for row in table_rows:
            columns = row.findChildren("td")
            
            date_col = columns[0]
            date_str = re.findall("(\d{1,2}\.\d{1,2}\.)", str(date_col))[0].strip()
            print(date_str)

            time_col = columns[1]
            time_str = time_col.string.split("\n")[1].strip()
            print(time_str)

            team_home_col = columns[2]
            team_home = team_home_col.findChild("a")
            team_home = str(team_home).split("\n")[3].strip()
            print(team_home)

            team_away_col = columns[4]
            team_away= team_away_col.findChild("a")
            team_away = str(team_away).split("\n")[3].strip()
            print(team_away)

            result_col = columns[6]
            result = result_col.findChild("a")
            result = str(result).split("\n")[1].split(":")
            home_goals = result[0]
            away_goals = result[1]
            print(f"Result was: {home_goals}:{away_goals}")




if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog="Handball Table Scraper", description="Scrapes gamedays's data.")
    parser.add_argument("-t", "--test", action="store_true", help="Uses old website data for faster development of parsing (instead of scraping).")

    args = parser.parse_args()
    main(testing = args.test)
