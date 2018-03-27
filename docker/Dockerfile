FROM python:2.7-jessie
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements/ /app/requirements
RUN pip install -r requirements/dev.txt
RUN touch /app/log
COPY . /app
RUN python manage.py migrate
