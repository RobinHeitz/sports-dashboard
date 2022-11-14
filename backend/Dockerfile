FROM python:latest

# Set working directory
WORKDIR /backend

COPY ./requirements.txt /backend
RUN pip install --no-cache-dir --upgrade -r requirements.txt

#Copy scripts to folder
COPY . /backend


#Run cmd:

# CMD ["python", "start_backend.py"]

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]


