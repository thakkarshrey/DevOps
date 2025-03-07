#!/bin/bash


USERS="alpha beta gamma"

for user in $USERS
do
	echo "####################"
	echo "Adding user $user"
	useradd $user
	id $user
	echo "####################"
done
