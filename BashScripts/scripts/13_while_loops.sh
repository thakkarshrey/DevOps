#!/bin/bash

counter=0

while [ $counter -lt 5 ]
do
	echo "The value of counter is $counter"
	counter=$(( $counter + 1 ))
	sleep 1
done
