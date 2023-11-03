from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import argparse
from bs4 import BeautifulSoup
import re

import datetime
from typing import Tuple, Optional, List
from pydantic import BaseModel
import enum

URL = "https://www.liquimoly-hbl.de/de/liqui-moly-hbl/spielplan/saisonen/spielplan/saison-23-24/spielplan-chronologisch/"

class HandballTeams(str, enum.Enum):
    berlin = "Füchse Berlin"
    scm = "SC Magdeburg"
    melsungen = "MT Melsungen"
    flensbug = "SG Flensburg-Handewitt"
    kiel = "THW Kiel"
    vfl = "VfL Gummersbach"
    loewen = "Rhein-Neckar Löwen"
    hannover = "TSV Hannover-Burgdorf"
    leipzig = "SC DHfK Leipzig"
    hamburg = "Handball Sport Verein Hamburg"
    bhc = "Bergischer HC"
    erlangen = "HC Erlangen"
    stuttgart = "TVB Stuttgart"
    lemgo = "TBV Lemgo Lippe"
    goeppingen = "FRISCH AUF! Göppingen"
    eisenach = "ThSV Eisenach"
    wetzlar = "HSG Wetzlar"
    balingen = "HBW Balingen-Weilstetten"



class GamePairing(BaseModel):

    class Config:
        use_enum_values = True

    start_time: datetime.time
    home_team: HandballTeams
    away_team: HandballTeams

    already_played: bool = False
    home_goals: Optional[int] = 0
    away_goals: Optional[int] = 0


class ScheduledGameday(BaseModel):
    date: datetime.date
    matches: List[GamePairing]

    def __str__(self):
        goals = sum(match.home_goals for match in self.matches) + sum(match.away_goals for match in self.matches)
        if goals > 0:
            avg = round(goals / len(self.matches) / 2,1)
            return f"Gameday: {self.date} with {len(self.matches)} matches with a total of {goals} goals (avg. per team = {avg})."
        return f"Gameday: {self.date} with {len(self.matches)} matches."


def main(testing=False, save_html=False):
    
    if testing is True:

        with open("example_html.txt", "r") as f:
            content = f.read()
    else:
        driver = webdriver.Chrome()
        driver.get(URL)
        content = driver.page_source

        if save_html is True:
            with open("new_content.txt", "w") as f:
                f.write(content)


    soup = BeautifulSoup(content, 'html.parser')
    scheduled_gamedays = soup.find_all('div', class_='schedule')

    print("**"*10)
    print("num scheduled days: ", len(scheduled_gamedays))
    print("**"*10)

    data = process_scheduled_gamedays(scheduled_gamedays)
    paired_matches_dict = parse_paired_matches(data)

    scheduled_gamedays = parse_date_of_matches(paired_matches_dict)
    for i in scheduled_gamedays:
        print(i)
    
    





def process_scheduled_gamedays(scheduled_gamedays) -> dict:
    data = {}
    
    for schedule in scheduled_gamedays:
        # print(schedule)
        table = schedule.findChild("table")
        schedule_head = table.findChild("thead").findChild("tr")

        table_body = table.findChild("tbody")
        table_rows = table_body.findChildren("tr")

        data[schedule_head] = table_rows
    return data


def parse_date_of_matches(parsed_matched:dict):
    
    scheduled_gamedays_list = []

    
    for table_head, matches in parsed_matched.items():
        date_str = re.findall("(\d{1,2}\.\d{1,2}\.)", str(table_head))[0]

        cur_year = datetime.datetime.now().year

        date = datetime.datetime.strptime(date_str, "%d.%m.").date()
        if 1 <= date.month <= 7:
            date = date.replace(year=cur_year + 1)
        else:
            date = date.replace(year=cur_year)

        scheduled_gamedays_list.append(
            ScheduledGameday(date=date, matches=matches)
        )

    return scheduled_gamedays_list


def parse_paired_matches(schedules:dict):
    
    matches_dict = {}

    for schedule_headline, matches in schedules.items():
        matches_list = []

        for match in matches:

            # Time Parsing
            columns = match.findChildren("td")
            time_col = columns[0]
            try:
                time_str = str(time_col).split("\n")[1].strip()
                match_time = datetime.datetime.strptime(time_str, "%H:%M").time()
            except:
                continue

            # Home and away team
            team_home_col = columns[1]
            team_home = team_home_col.findChild("a")
            team_home = str(team_home).split("\n")[3].strip()
      
            team_away_col = columns[3]
            team_away = team_away_col.findChild("a")
            team_away = str(team_away).split("\n")[3].strip()

            # goals
            result_col = columns[5]
            result = result_col.findChild("a")
            if result is None:
                game_pairing = GamePairing(start_time=match_time, home_team=team_home, away_team=team_away)
            
            else:
                result = str(result).split("\n")[1].split(":")
                home_goals = result[0]
                away_goals = result[1]
                game_pairing = GamePairing(
                    start_time=match_time,
                    home_team=team_home,
                    away_team=team_away,
                    already_played=True,
                    home_goals=home_goals,
                    away_goals=away_goals,
                    )

            matches_list.append(game_pairing)
        
        if len(matches_list) > 0:
            matches_dict[schedule_headline] = matches_list
    return matches_dict
    




if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog="Handball Table Scraper", description="Scrapes gamedays's data.")
    parser.add_argument("-t", "--test", action="store_true", help="Uses old website data for faster development of parsing (instead of scraping).")
    parser.add_argument("-s", "--save_html", action="store_true", help="Save html content in a .txt file. Has no effect with -t.")

    args = parser.parse_args()
    main(testing = args.test, save_html=args.save_html)