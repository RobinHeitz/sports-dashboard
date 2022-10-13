from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path
from functools import partial

from handball.definitions_hb import HandballStanding
import handball.handball as hb

from football.definitions_fb import FootballStanding
import football.football as fb

import yaml


with open(Path("config.yaml")) as f:
    config = yaml.safe_load(f).get("testing")

print("*"*10)
print(config)

class DataType():
    hb_cl = "hb_cl"
    hb_bl = "hb_bl"
    fb_bl = "fb_bl"
    fb_cl = "fb_cl"


data_store_updater = {
    DataType.fb_bl: fb.get_bl_standing,
    DataType.fb_cl: fb.get_cl_standing,
    DataType.hb_bl: hb.get_bl_standing,
}


data_store = {
    DataType.fb_bl: "Init FB BL",
    DataType.fb_cl: "Init FB CL", 
    DataType.hb_bl: "Init HB CL",
}


def update_data_store():
    global data_store
    for key in data_store_updater:
        testing = config.get(key, True)
        func = data_store_updater.get(key, lambda: "")
        data_store[key] = func(testing = testing)

update_data_store()

##################
### API BEGINS ###
##################

app = FastAPI()

@app.get("/handball/standing/bl")
def get_hb_bl_standings():
    return data_store.get(DataType.hb_bl)

@app.get("/handball/standing/cl")
def get_hb_bl_standings():
    return data_store.get(DataType.hb_bl)



@app.get("/football/standing/bl")
def get_fb_bl_standings():
    return data_store.get(DataType.fb_bl)

@app.get("/football/standing/cl")
def get_fb_bl_standings():
    return data_store.get(DataType.fb_cl)

@app.get("/")
def get_root():
    return f"This is my little sports-api for handball and football data (bl and cl).To get an overview, look at: /docs. {config=}"