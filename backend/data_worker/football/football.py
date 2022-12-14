# %%
from typing import Protocol, List
from urllib import response

import requests
import json
from .definitions_fb import FootballStanding, FootballTypeEnum

from pathlib import Path

### Config
HEADERS = {"X-Auth-Token":"516f434d1e4b46a993b63380d4882fa7"}


def _dir_test_data(file_name:str) -> Path:
    p = Path("football/test_data")
    if not p.exists():
        p = Path("test_data")
    return p / file_name

def get_bl_standing(testing = True) ->FootballStanding:
    """Returns a list of FootballStanding - Objects which represents current 1. Bundesliga standings.
    Params: 
    - testing (default = True): If true, fakes call by reading data from a file.
    """
    if testing == True:
        json_data = __get_standings_data_testing(_dir_test_data("football_bl1.txt"))
    else:
        json_data = __get_standings_data_api("https://api.football-data.org/v4/competitions/BL1/standings")
    return __validate_standings_data(json_data)


def get_cl_standing(testing = True) -> FootballStanding:
    """Returns a list of FootballStanding - Objects which represents current UEFA Champions League standings.
    Params: 
    - testing (default = True): If true, fakes call by reading data from a file.
    """
    if testing == True:
        json_data = __get_standings_data_testing(_dir_test_data("football_cl.txt"))
    else:
        json_data = __get_standings_data_api("https://api.football-data.org/v4/competitions/CL/standings")
    return __validate_standings_data(json_data)




def __get_standings_data_testing(path:Path):
    """Reads and parses data as json from a given path. This is for testing purpose."""
    with open(path) as f:
        json_data = json.load(f)
    return json_data


def __get_standings_data_api(url):
    """Returns json data from API of given url."""
    if url == None:
        raise ValueError("Url-Argument shouldn't be None if offline_data is False.")
    response = requests.get(url=url, headers=HEADERS)
    return response.json()



def __validate_standings_data(json_data) -> List[FootballStanding]:
    """Validates json data by using pydantic model structure."""
    standings_json = json_data.get("standings")
    standings = [FootballStanding(**s) for s in standings_json]
    standings = list(filter(lambda s: s.type == FootballTypeEnum.TOTAL, standings))
    return standings




if __name__ == "__main__":
    ...



    