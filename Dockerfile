FROM python:latest

# Set working directory
WORKDIR /app

COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

#Copy scripts to folder
COPY . /app


#Run cmd:

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]


