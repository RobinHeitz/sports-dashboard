# Dashboard for seeing sport results/ tables/ upcomming matches.

## Information running selenium on headless-pi
https://stackoverflow.com/questions/64979042/how-to-run-seleniumchrome-on-raspberry-pi-4

## Using free API from:
https://www.football-data.org/documentation/quickstart


## Selenium Setup:
Get Webdriver (from selenium website) with the corresponding version of your browser and unpack it.
Copy to /usr/local/bin (for mac at least).


# FastApi:
Run the local server with:
uvicorn main:app --reload
API-Documentation: http://127.0.0.1:8000/docs

# Build & Run Docker images (for deployment)
docker build -t sports-api .
docker run -d -p 8000:80 sports-api

# Docker Compose for development (NO DEPLOYMENT:
docker-compose up --build
