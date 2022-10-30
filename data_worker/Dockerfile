FROM python:latest

# Set working directory
WORKDIR /data_worker

COPY data_worker/requirements.txt /data_worker
RUN pip install --no-cache-dir --upgrade -r requirements.txt

#Copy scripts to folder
COPY . /data_worker

# Copy pkg common

# COPY ../common /data_worker


#Run cmd:

CMD ["python", "main.py"]


