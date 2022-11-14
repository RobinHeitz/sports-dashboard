FROM python:latest

# Set working directory
WORKDIR /scraper

COPY ./requirements.txt /scraper
RUN pip install --no-cache-dir --upgrade -r requirements.txt

#Copy scripts to folder
COPY . /scraper


#Run cmd:

CMD ["python", "start_scraping.py"]
