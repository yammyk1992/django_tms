FROM python:3.9-alpine3.16

# set work directory
WORKDIR /PycharmProject/django_tms/
COPY ./requirements.txt .
COPY . .
EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

# copy project

RUN pip install -r requirements.txt
RUN adduser --disabled-password service-user


USER service-user
