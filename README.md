# Main project folder

Within this, there are the following packages, each deploys with its own docker-container.


# Build & Run Docker images (for deployment)
docker build -t sports-api .
docker run -d -p 8000:80 sports-api

# Docker Compose for development (NO DEPLOYMENT:
docker-compose up --build


## webserver
Webserver is using SQLAlchemy + Alembic for managing a sqlite-db.

### Start webserver:
docker-compose up
if re-build is needed (new dependencies):
docker-compose up --build

### FastApi:
Run the local server with:
uvicorn main:app --reload
API-Documentation: http://127.0.0.1:8000/docs

### Migrate changes in data model:
alembic revision --autogenerate -m "My revision text"
alembic upgrade head



## data_worker
Performs job of receiving new data from api's or web scraping and sends it to the webserver
### Information running selenium on headless-pi
https://stackoverflow.com/questions/64979042/how-to-run-seleniumchrome-on-raspberry-pi-4

### Using free API from:
https://www.football-data.org/documentation/quickstart

### Selenium Setup:
Get Webdriver (from selenium website) with the corresponding version of your browser and unpack it.
Copy to /usr/local/bin (for mac at least).



