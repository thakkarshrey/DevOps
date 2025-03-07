#!/bin/bash


user="devops"

for host in `cat remoteHosts.txt`
do
	echo
	echo "############################"
	echo "Connecting to host : $host"
	echo "Pushing the script to $host"
	scp multios_websetup.sh $user@$host:/tmp/
	echo "Executing the script for host : $host"
	ssh $user@$host sudo /tmp/multios_websetup.sh
	echo "Cleaning up trash"
	ssh $user@$host sudo rm -rf /tmp/multios_websetup.sh
	echo "############################"
	echo
done
