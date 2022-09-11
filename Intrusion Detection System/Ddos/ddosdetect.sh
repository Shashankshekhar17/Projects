#!/bin/bash

echo "<-----Checking------>"
sleep 2
ref=08000
chektime=$( { time ping asfaa.org -c 4; } 2>&1 |grep "real" | awk '{print $2}' | awk -F m '{print $1$2}' | awk -F s '{print $1}' | awk -F . '{print $1$2}' )
echo " "
if [ "$chektime" -gt "$ref" ]; then 
 echo "Ddos Detected"
else 
 echo "Server is Up and Running"
fi