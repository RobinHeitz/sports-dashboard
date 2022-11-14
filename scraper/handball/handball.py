from time import sleep
from bs4 import BeautifulSoup, ResultSet

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement

from pyvirtualdisplay import Display

from .definitions_hb import HandballPosition, HandballStageEnum, HandballStanding, HandballTypeEnum

from pathlib import Path

from typing import List


def _get_html_from_website(url:str, xpath:str):
    """Using seleniums webdriver for returning website's html code for given url and x-path."""
    display = Display(visible=False, size=(1024,768))
    display.start()

    chromeOptions = Options()
    chromeOptions.headless = True
    
    browser = webdriver.Chrome(options=chromeOptions)
    browser.get(url)
    sleep(2)
    table:webelement.WebElement = browser.find_element(By.XPATH,xpath)
    html_code = table.get_attribute("innerHTML")
    
    browser.quit()
    display.stop()
    
    return html_code


def _parse_positions_from_html_code(rows:ResultSet) -> List[HandballPosition]:
    positions = []

    attrs = (
        dict(attr_key = "position", parse_f = lambda e: list(e.children)[-1]), 
        dict(attr_key = "team", parse_f = lambda e: e.find("a").contents[-1].strip("\n")), 
        dict(attr_key = "played_games", ),
        dict(attr_key = "won", ),
        dict(attr_key = "draw",),
        dict(attr_key = "lost",),
        dict(attr_key = "points",),
        dict(attr_key = "goal_difference",),
        dict(attr_key = "goals_for",), 
        dict(attr_key = "goals_against",),
    )
    for row in rows:
        tds = row.find_all("td")

        current_team = dict()
        for index, item in enumerate(tds):
            attr = attrs[index]
            parse_function = attr.get("parse_f", lambda e:e.string)
            current_team[attr.get("attr_key")] = parse_function(item)

        handball_pos = HandballPosition(**current_team)

        positions.append(handball_pos)
        return positions



def get_bl_standing(url:str, xpath:str) -> HandballStanding:
    """Returns """
    html_code = _get_html_from_website(url, xpath)

    soup = BeautifulSoup(html_code, "html.parser")
    rows = soup.find_all("tr")
    
    positions = _parse_positions_from_html_code(rows)

    return HandballStanding(
        competition_name="Liquimoly Handball-Bundesliga",
        table = positions, 
        type=HandballTypeEnum.TOTAL,
        stage=HandballStageEnum.REGULAR_SEASON,
    )