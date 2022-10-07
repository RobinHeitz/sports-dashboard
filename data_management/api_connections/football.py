# %%
from typing import Protocol, List

import requests
import json

from pydantic import BaseModel, Field, ValidationError, validator, root_validator



# class Test(BaseModel):
#     @root_validator(pre=True)

#     def testing(cls, values):
#         ...
#         print("values = ", values, "/// team = ", values.get("team"))
        
#         team_dict = values.pop("team")

#         returnDict =  {**values, "team": team_dict.get("name")}
#         print("RETURN DICT = ", returnDict)
#         return returnDict


#     identifier: int = Field(..., alias="id") # ... === Field is required
#     team: str = Field(..., alias = "team")



 

class Standing(BaseModel):
    position: int
    team: str
    played_games: int = Field(..., alias="playedGames")
    won:int
    draw:int
    lost:int
    points: int
    goals_for: int  = Field(..., alias="goalsFor")
    goals_against:int = Field(..., alias="goalsAgainst")
    goal_difference:int = Field(..., alias="goalDifference")

    @root_validator(pre=True)
    def flatten_data_structure(cls, values):
        ...
        team = values.pop("team")
        return {**values, "team": team.get("name")}




    
def get_request_data():
    ...
    URL = "https://api.football-data.org/v4/competitions/BL1/standings"
    response = requests.get(url=URL, headers={"X-Auth-Token":"516f434d1e4b46a993b63380d4882fa7"})

    return response.json()


if __name__ == "__main__":
    ...
    data = get_request_data()
    standings = data.get("standings")

    for s in standings:
        if s.get("type") == "TOTAL":
            standings = s
    
    table = standings.get("table")

    standing_objects: List[Standing] = []
    for t in table:
        standing_objects.append(
            Standing(**t)
        )
    
    print(standing_objects)



    


   

    