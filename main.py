import argparse
import scraper.handball.handball as hb_scraper

URL_BL_GAME_DATES = "https://www.liquimoly-hbl.de/de/liqui-moly-hbl/spielplan/saisonen/spielplan/saison-23-24/spielplan-nach-spieltagen/"


def read_offline_html() -> str:
    path = "scraper/handball/test_table_body.txt"
    with open(path, "r") as f:
        html_code = f.read()
    return html_code


def main(testing):
    xpath = ""
    # if testing is True:
    #     html_code = read_offline_html()
    # else:
    #     html_code = hb_scraper.get_html_from_website(URL_BL_GAME_DATES, xpath)

    # standings = hb_scraper.get_bl_standing(html_code)
    # print(standings)
    # print(html_code)

    






if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument("-t", "--test", action="store_true", help="Use offline html code instead.")

    args = parse.parse_args()
    main(testing=args.test)