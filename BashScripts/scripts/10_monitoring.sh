#!/bin/bash

echo "####################################"
date
ls /var/run/httpd/httpd.pid &> /dev/null

if [ $? -eq 0 ]
then
	echo "Httpd process is running."
else
	echo "Httpd process is not running."
	echo "Starting httpd service!"
	sudo systemctl start httpd

	if [ $? -eq 0 ]
	then
		echo "Service started successfully!"
	else
		echo "Starting the process failed."
	fi
fi
echo "####################################"
echo
