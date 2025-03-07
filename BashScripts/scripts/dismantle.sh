#!/bin/bash

sudo systemctl stop httpd
sudo rm -rf /var/www/html/*
sudo yum remove wget zip unzip httpd -y

