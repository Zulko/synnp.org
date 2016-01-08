#!/usr/bin/env bash

# install pip if it doesn't exist yet
which pip > /dev/null 2>&1
if [ $? -ne 0 ]; then
    sudo apt-get install -q -y python-pip
fi


# install python development headers
dpkg --get-selections | grep python-dev > /dev/null 2>&1
if [ $? -ne 0 ]; then
    sudo apt-get update
    sudo apt-get install -q -y python-dev
fi


# install ffi for bcrypt
dpkg --get-selections | grep libffi-dev > /dev/null 2>&1
if [ $? -ne 0 ]; then
    sudo apt-get install -q -y libffi-dev
fi


# install pq
dpkg --get-selections | grep libpq-dev > /dev/null 2>&1
if [ $? -ne 0 ]; then
    sudo apt-get install -q -y libpq-dev
fi


sudo apt-get install -q -y postgresql postgresql-contrib
sudo apt-get install -q -y nginx

# install requirements from pip requirements file

# Version on PyPI of django-registration is buggy, using the github repo instead
#sudo pip install django-registration-redux
sudo pip install git+git://github.com/macropin/django-registration.git

sudo pip install django-compressor

# Version on PyPI of django-spaghetti-and-meatballsn is buggy, using the github repo instead
#sudo pip install django-spaghetti-and-meatballs
sudo pip install git+git://github.com/LegoStormtroopr/django-spaghetti-and-meatballs.git

sudo pip install gunicorn