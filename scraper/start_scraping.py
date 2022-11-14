import toml
from pathlib import Path
import threading
import requests

from handball import handball


HANDBALL_BL = "handball_bl"


def main():
    ...
    p = Path("config.toml")
    with open(p) as f:
        config = toml.load(f)
    
    scrape_handball_bl(config.get(HANDBALL_BL))



def scrape_handball_bl(hb_config):
    print("scrape_handball_bl")

    testing = hb_config.get("testing", False)
    url = hb_config.get("url")
    xpath = hb_config.get("xpath")

    print(f"{url=}| {testing=} | {xpath=}")

    handball.get_bl_standing(url, xpath)







if __name__ == "__main__":
    main()











