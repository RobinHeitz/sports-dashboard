# Main project folder

Within this, there are the following packages, each deploys with its own docker-container.

## webserver
Webserver is using SQLAlchemy + Alembic for managing a sqlite-db.

### Start webserver:
docker-compose up
if re-build is needed (new dependencies):
docker-compose up --build


### Migrate changes in data model:
alembic revision --autogenerate -m "My revision text"
alembic upgrade head

## data_worker
Performs job of receiving new data from api's or web scraping and sends it to the webserver