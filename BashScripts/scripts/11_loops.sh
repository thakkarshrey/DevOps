#!/bin/bash

for VAR in frontend backend react nodejs
do
	echo "Looping"
	date
	echo "##########################"
	echo "Value of var is $VAR"
	echo "##########################"
	sleep 1
	echo
done


for (( c=1; c<=5; c++ ))
do
        echo "##########################"
        echo "Printing the numbers : $c"
        echo "##########################"
        echo
done
