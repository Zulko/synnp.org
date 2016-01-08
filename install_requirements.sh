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
sudo pip install django-registration-redux
sudo pip install django-spaghetti-and-meatballs
sudo pip install gunicorn