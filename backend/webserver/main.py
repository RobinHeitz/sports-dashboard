from fastapi import FastAPI
from common import schemas

from data_management import model, data_controller


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

@app.get("/")
def get_root():
    return f"This is my little sports-api for handball and football data (bl and cl).To get an overview, look at: /docs."

########################
### GET DATA FROM DB ###
########################

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


@app.get("/testing")
def get_test_data():
    ...

    with data_controller.session_context() as session:
        query = session.query(model.Competition).all()
        return f"Competition-instances in db: {query=}"


#####################
### POST NEW DATA ###
#####################

@app.post("/handball/standing/bl")
def post_hb_bl_standing(new_standing: schemas.Standing):
    # dc.create_standing(new_standing)
    ...
    