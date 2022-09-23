# %%
from cmath import pi
from typing import Protocol
import requests

BASE_URL = "https://api.football-data.org/v4/"

def get_areas():
    url = f"{BASE_URL}areas/"

    response = requests.get(url)
    
    data = response.json()
    areas = data.get("areas", dict())

    europe = list(filter(lambda area: area.get("parentArea", "") == "Europe", areas))

    print(europe)


def get_competitions():
    url = f"{BASE_URL}competitions/"

    payload = dict(areas = [2077])

    resp = requests.get(url, params=payload)
    data = resp.json()

    test = [league for league in data.get("competitions") if league.get("code") == "CL"]

    print(test)

def get_CL():
    url = f"{BASE_URL}/competitions/CL"
    resp = requests.get(url)
    data = resp.json()

    print(data)
    


class SportDataClass(Protocol):
    def get_data():
        raise NotImplementedError("Protocol class should not be implemented.")

if __name__ == "__main__":
    # get_areas()
    # get_CL()
    get_competitions()