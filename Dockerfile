FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /webapps
COPY requirements.txt /webapps
RUN pip install -r requirements.txt
COPY . /webapps