#!/bin/bash

echo "Please enter a number : "
read NUM

if [ $NUM -gt 100 ]
then
	echo "Number is greater than 100"
else
	echo "Number is less than 100"
fi

echo

echo "Script execution completed!"
