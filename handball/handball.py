from time import sleep
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement

from .definitions_hb import HandballPosition, HandballStageEnum, HandballStanding, HandballTypeEnum

from pathlib import Path

def _get_test_file_path()-> Path:
    """Depending on which directory in console handball.py gets started, path needs to change."""
    path = Path("handball/test_table_body.txt")
    if path.exists():
        return path
    return Path("test_table_body.txt")


def _bl_standings_html_code(testing = True):
    if testing == True:
        path = _get_test_file_path()
        with open(path) as f:
            lines =  "".join(f.readlines())
            return lines

    url = "https://www.liquimoly-hbl.de/de/liqui-moly-hbl/tabelle/saisonen/tabelle/saison-22-23/gesamt-tabelle/"
    table_body_xpath = '//*[@id="standings2028776"]/div/table/tbody'
    return _get_html_from_website(url,table_body_xpath)




def _get_html_from_website(url:str, xpath:str):
    """Using seleniums webdriver for returning website's html code for given url and x-path."""
    browser = webdriver.Chrome()
    browser.get(url)
    sleep(2)
    table:webelement.WebElement = browser.find_element(By.XPATH,xpath)
    html_code = table.get_attribute("innerHTML")
    return html_code



def get_bl_standing(testing = True) -> HandballStanding:
    """Returns """

    html_code = _bl_standings_html_code(testing = testing)
    soup = BeautifulSoup(html_code, "html.parser")
    rows = soup.find_all("tr")

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

    positions = list()

    for row in rows:
        tds = row.find_all("td")

        current_team = dict()
        for index, item in enumerate(tds):
            attr = attrs[index]
            parse_function = attr.get("parse_f", lambda e:e.string)
            current_team[attr.get("attr_key")] = parse_function(item)

        handball_pos = HandballPosition(**current_team)

        positions.append(handball_pos)
    


    standings =  HandballStanding(
        competition_name="Liquimoly Handball-Bundesliga",
        table = positions, 
        type=HandballTypeEnum.TOTAL,
        stage=HandballStageEnum.REGULAR_SEASON,
    )
    print(standings)
    return standings

get_cl_standing = get_bl_standing

if __name__ == "__main__":
    get_bl_standing(testing=True)