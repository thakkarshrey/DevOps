#!/bin/bash

echo "Welcome $USER on $HOSTNAME"
echo "#######################################"

FREE_RAM=$(free -m | grep Mem | awk '{print $4}')
LOAD=`uptime | awk '{print $9}'`
ROOT_FREE=`df -h | grep '/dev/sda1' | awk '{print $4}'`

echo "#######################################"
echo "The free RAM available is $FREE_RAM"


echo "#######################################"
echo "The load is $LOAD"
echo "#######################################"



echo "#######################################"
echo "The free root partition available is $ROOT_FREE"
echo "#######################################"
