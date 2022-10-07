##########################
# API: football-data.org #
##########################

import requests
import enum

# (Competition_ID, League-Code, Caption, Country)

uk_pl = 2021, "PL", "Premier League", "England"

eu_uefa_cl = 2001, "CL", "UEFA Champions League", "Europe"

de_bl = 2002, "BL1", "Bundesliga", "Germany"

it_seriea = 2019, "SA", "Serie A", "Italy"

esp_pd = 2014, "PD", "Primera Division", "Spain"

BASE_URL = "https://api.football-data.org/v4/"

API_TOKEN = "516f434d1e4b46a993b63380d4882fa7"

uri = 'https://api.football-data.org/v4/matches'
headers = { 'X-Auth-Token': 'UR_TOKEN' }

response = requests.get(uri, headers=headers)
for match in response.json()['matches']:
    print(match)


class Competition(enum.Enum):
    UEFA_CL = enum.auto()
    BL = enum.auto()
    PL = enum.auto()


competition_codes = {
    Competition.UEFA_CL: dict(
        id = 2001,
    ),

    Competition.BL: dict(

    ),

    Competition.PL: dict(

    ),


}







def get_data_from_get(url: str):
    response = requests.get(url, )
    status = response.status_code




HEADER = "X-Auth-Token"
API_TOKEN = "516f434d1e4b46a993b63380d4882fa7"
