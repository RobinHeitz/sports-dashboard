from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path
from functools import partial




##################
### API BEGINS ###
##################

data_store = {
    "hb_bl": "hb Bl =)",
    "hb_cl": "Hi this is hb Cl",
    "fb_bl": "Hi this is FB Bl",
    "fb_cl": "Hi this is FB UEFA CL",
}

app = FastAPI()

@app.get("/handball/standing/bl")
def get_hb_bl_standings():
    return data_store.get("hb_bl")

@app.get("/handball/standing/cl")
def get_hb_bl_standings():
    return data_store.get("hb_cl")

@app.get("/football/standing/bl")
def get_fb_bl_standings():
    return data_store.get("fb_bl")

@app.get("/football/standing/cl")
def get_fb_bl_standings():
    return data_store.get("fb_cl")

@app.get("/")
def get_root():
    return f"This is my little sports-api for handball and football data (bl and cl).To get an overview, look at: /docs."