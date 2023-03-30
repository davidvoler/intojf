FROM python:3.8.3-slim-buster
RUN mkdir /app
WORKDIR /app
RUN pip install --upgrade pip
COPY  requirements.txt . 
RUN pip install -r requirements.txt
COPY app_config .
WORKDIR /app/app_config
RUN python setup.py sdist
RUN twine upload dist/*
