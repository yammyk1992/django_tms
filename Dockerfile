FROM python:3.10-alpine3.16

# set work directory
WORKDIR /PycharmProject/django_tms/


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .
