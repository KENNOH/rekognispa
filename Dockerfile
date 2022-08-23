ARG PROJECT_PATH=/usr/share/webapps/rekognispa

FROM python:3
ENV PYTHONUNBUFFERED=1
ARG PROJECT_PATH
WORKDIR ${PROJECT_PATH}
COPY requirements.txt ${PROJECT_PATH}
RUN pip install -r requirements.txt
COPY . ${PROJECT_PATH}
RUN python manage.py migrate --no-input --run-syncdb
RUN python manage.py collectstatic --no-input
