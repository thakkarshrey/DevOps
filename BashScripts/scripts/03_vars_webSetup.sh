#!/bin/bash

# Variable declaration
PACKAGE="wget zip unzip httpd"
URL="https://www.tooplate.com/zip-templates/2132_clean_work.zip"
WEBSITE_FOLDER_NAME="2132_clean_work"
TEMPDIR="/tmp/webfiles"
SERVICE="httpd"


# Installing dependencies
echo "######################################"
echo "Installing dependencies"
echo "######################################"

sudo yum install $PACKAGE -y > /dev/null
echo

# Start and enable httpd service
echo "######################################"
echo "Start and Enable httpd service"
echo "######################################"

sudo systemctl start $SERVICE
sudo systemctl enable $SERVICE
echo


# Creating temporary files
echo "######################################"
echo "Creating temporary files"
echo "######################################"

sudo mkdir -p $TEMPDIR
cd $TEMPDIR
wget $URL > /dev/null
sudo unzip $WEBSITE_FOLDER_NAME.zip
echo


# Copying files to the /var/www/html directory
echo "######################################"
echo "Copying files to right place"
echo "######################################"

sudo cp -r $WEBSITE_FOLDER_NAME/* /var/www/html
sudo systemctl restart $SERVICE
echo

# Trash clean up
echo "######################################"
echo "Trash clean up"
echo "######################################"

sudo rm -rf $TEMPDIR
ls /var/www/html
sudo systemctl status $SERVICE
echo
