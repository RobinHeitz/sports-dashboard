# FROM --platform=linux/arm64 python:3.11
FROM --platform=linux/arm64 alpine

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt -y update
RUN apt install -y chromium
RUN apt -y install xvfb 

# install chromedriver
RUN apt install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# set display port to avoid crash
ENV DISPLAY=:99

WORKDIR /scraper


COPY ./requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

# # Set working directory & copy the stuff there
# WORKDIR /scraper
# COPY . /scraper

# #Run cmd:
CMD ["python3", "start_scraping.py"]

