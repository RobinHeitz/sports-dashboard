FROM python:latest

# Set working directory
WORKDIR /web

COPY ./requirements.txt /web
RUN pip install --no-cache-dir --upgrade -r requirements.txt

#Copy scripts to folder
COPY . /web


#Run cmd:

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]


