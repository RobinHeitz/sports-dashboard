from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import argparse
from bs4 import BeautifulSoup

from handball.definitions import HandballTeamsBundesliga, HandballTeamsChampionsLeague
from handball.definitions import GamePairing, ScheduledGameday

from handball.parse_bundesliga import process_scheduled_gamedays, parse_date_of_matches, parse_paired_matches

import yaml


def main(testing=False, save_html=False):
    
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
    
    content_hbl = get_website_content(testing, save_html, config["handball_bl"])

    scheduled_gamedays_bundesliga = process_handball_bundesliga(content_hbl)
    for i in scheduled_gamedays_bundesliga:
        print(i)



def get_website_content(testing, save_html, config):
    offline_filename = config["offline_filename"]
    if testing is True:

        with open(offline_filename, "r") as f:
            content = f.read()
    else:
        url = config["url"]
        
        driver = webdriver.Chrome()
        driver.get(url)
        content = driver.page_source

        if save_html is True:
            with open(offline_filename, "w") as f:
                f.write(content)
    return content



def process_handball_bundesliga(content):

    soup = BeautifulSoup(content, 'html.parser')
    scheduled_gamedays = soup.find_all('div', class_='schedule')

    data = process_scheduled_gamedays(scheduled_gamedays)
    paired_matches_dict = parse_paired_matches(data)

    scheduled_gamedays = parse_date_of_matches(paired_matches_dict)
    return scheduled_gamedays
    


if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog="Handball Table Scraper", description="Scrapes gamedays's data.")
    parser.add_argument("-t", "--test", action="store_true", help="Uses old website data for faster development of parsing (instead of scraping).")
    parser.add_argument("-s", "--save_html", action="store_true", help="Save html content in a .txt file. Has no effect with -t.")

    args = parser.parse_args()
    main(testing = args.test, save_html=args.save_html)