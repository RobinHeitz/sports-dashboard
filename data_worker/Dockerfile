FROM python:latest

# Set working directory
WORKDIR /data_worker

COPY ./requirements.txt /data_worker
RUN pip install --no-cache-dir --upgrade -r requirements.txt

#Copy scripts to folder
COPY . /data_worker


#Run cmd:

CMD ["python", "main.py"]


