#!/bin/bash

# Installing dependencies
echo "######################################"
echo "Installing dependencies"
echo "######################################"

sudo yum install wget unzip httpd zip -y > /dev/null
echo

# Start and enable httpd service
echo "######################################"
echo "Start and Enable httpd service"
echo "######################################"

sudo systemctl start httpd
sudo systemctl enable httpd
echo


# Creating temporary files
echo "######################################"
echo "Creating temporary files"
echo "######################################"

sudo mkdir -p /tmp/webfiles
cd /tmp/webfiles
wget https://www.tooplate.com/zip-templates/2132_clean_work.zip > /dev/null
sudo unzip 2132_clean_work.zip
echo


# Copying files to the /var/www/html directory
echo "######################################"
echo "Copying files to right place"
echo "######################################"

sudo cp -r 2132_clean_work/* /var/www/html
sudo systemctl restart httpd
echo

# Trash clean up
echo "######################################"
echo "Trash clean up"
echo "######################################"

sudo rm -rf /tmp/webfiles
ls /var/www/html
sudo systemctl status httpd
echo
