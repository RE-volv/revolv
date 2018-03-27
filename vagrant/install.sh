#!/bin/bash

# Script to set up a Django project on Vagrant.

DATABASE_USERNAME="revolv"
DATABASE_PASSWORD="revolv"
DATABASE_NAME="revolv_db"
PGSQL_VERSION=9.3

cd /vagrant

# Need to fix locale so that Postgres creates databases in UTF-8
locale-gen en_GB.UTF-8
dpkg-reconfigure locales

apt-get update -y
apt-get install -y git

# Postgresql
apt-get install -y postgresql-$PGSQL_VERSION libpq-dev
cp /vagrant/vagrant/pg_hba.conf /etc/postgresql/$PGSQL_VERSION/main/
service postgresql restart

# Python
apt-get install -y build-essential python python-dev python-setuptools
easy_install -U pip
pip install -U virtualenv
virtualenv venv -p `which python2.7`
source venv/bin/activate
pip install -r requirements/dev.txt

# Node.js and npm
apt-get --purge remove node
apt-get autoremove
curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -
apt-get install -y nodejs

sudo -u postgres psql -c "create database $DATABASE_NAME;"
sudo -u postgres psql -c "create user $DATABASE_USERNAME with password '$DATABASE_PASSWORD';"
sudo -u postgres psql -c "grant all privileges on database $DATABASE_NAME to $DATABASE_USERNAME;"
sudo -u postgres psql -c "alter user $DATABASE_USERNAME createdb;"

npm install
cp revolv/settings/local.example.py revolv/settings/local.py
echo "DJANGO_SETTINGS_MODULE=revolv.settings.local" > .env
python manage.py migrate
