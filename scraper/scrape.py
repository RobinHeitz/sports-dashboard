from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import argparse
from bs4 import BeautifulSoup
import yaml

from typing import List

from handball.definitions import HandballTeamsBundesliga, HandballTeamsChampionsLeague
from handball.definitions import Match, ScheduledGameday

from handball.parse_bundesliga import process_scheduled_gamedays, parse_date_of_matches, parse_paired_matches
from handball.parse_cl import process_scheduled_matches_cl, process_scheduled_gamedays_cl

from pathlib import Path

def main(**kwargs):

    config_path = Path(__file__).parent / "config.yaml"
    
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    if kwargs["bl_off"] == False:
        print("=== Start processing bundesliga")
        content_hbl = get_website_content(config = config["handball_bl"], **kwargs)
        gamedays_bundesliga = process_handball_bundesliga(content_hbl)
        print_gamedays(gamedays_bundesliga)

    if kwargs["cl_off"] == False:
        print("=== Start processing champions league")
        content_cl = get_website_content(config = config["handball_cl"], exec_driver_func = click_button_load_more_matches, **kwargs)
        gamedays_cl = process_handball_championsleague(content_cl)
        print_gamedays(gamedays_cl)


def print_gamedays(gamedays: List[ScheduledGameday]):
    for gameday in gamedays:
        print(f"====== New gameday on {gameday.date} with {len(gameday.matches)} matches:")
        for index, match in enumerate(gameday.matches):
            if match.already_played:
                print(f"={index +1}: {match.home_team} - {match.home_goals} vs {match.away_goals} - {match.away_team}")
            else:
                print(f"={index +1}: {match.home_team} vs {match.away_team}")


def click_button_load_more_matches(driver):
    """Function gets invoked only in CL parsing, because there are plenty matches hidden behind button clicks. Classname: 'load-more-matches'."""
    while True:

        try:
            load_more_matches_btn = driver.find_element(By.CLASS_NAME, "load-more-matches")
            driver.execute_script("arguments[0].click();", load_more_matches_btn)
        except:
            break



def get_website_content(testing, save_html, config, **kwargs):
    offline_filename = config["offline_filename"]
    path = Path(__file__).parent / offline_filename

    if testing is True:

        with open(path, "r") as f:
            content = f.read()
    else:
        url = config["url"]
        
        driver = webdriver.Chrome()
        driver.get(url)

        if 'exec_driver_func' in kwargs:
            print("=== Start executing driver function.")
            func = kwargs['exec_driver_func']
            func(driver)

        content = driver.page_source

        if save_html is True:
            with open(path, "w") as f:
                f.write(content)
    return content



def process_handball_bundesliga(content):
    soup = BeautifulSoup(content, 'html.parser')
    scheduled_gamedays = soup.find_all('div', class_='schedule')

    data = process_scheduled_gamedays(scheduled_gamedays)
    paired_matches_dict = parse_paired_matches(data)

    scheduled_gamedays = parse_date_of_matches(paired_matches_dict)
    return scheduled_gamedays



def process_handball_championsleague(content):
    soup = BeautifulSoup(content, 'html.parser')
    scheduled_games = soup.find_all('a', class_="table-row table-row--results")
    matches = process_scheduled_matches_cl(scheduled_games)
    gamedays = process_scheduled_gamedays_cl(matches)
    # gamedays
    return gamedays



if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog="Handball Table Scraper", description="Scrapes gamedays's data.")
    parser.add_argument("-t", "--test", action="store_true", help="Uses old website data for faster development of parsing (instead of scraping).")
    parser.add_argument("-s", "--save_html", action="store_true", help="Save html content in a .txt file. Has no effect with -t.")
    parser.add_argument("-b", "--bl_off", action="store_true", help="Turns off bundesliga parsing.")
    parser.add_argument("-c", "--cl_off", action="store_true", help="Turns off champions league parsing.")

    args = parser.parse_args()
    main(testing = args.test, save_html=args.save_html, bl_off = args.bl_off, cl_off = args.cl_off)