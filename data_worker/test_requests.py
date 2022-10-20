# %%
import requests
import common.schemas as schemas

from datetime import datetime


p1 = schemas.Position(position=1, team="My Team 1", played_games=12, won=11, draw=1, lost=2, points="14:0", goal_difference=33, goals_for=123, goals_against=22)
p2 = schemas.Position(position=2, team="My Team 2", played_games=11, won=9, draw=1, lost=4, points="11:3", goal_difference=14, goals_for=199, goals_against=40)
s = schemas.Standing(positions=[p1, p2], updated=datetime.now())

resp = requests.post("http://localhost:8000/handball/standing/bl", data = s.json())

print(resp.text)
print(resp.status_code)
print(resp.json())

