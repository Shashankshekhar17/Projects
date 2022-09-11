#!/bin/bash

echo "<-----Checking------>"
sleep 2
ref=08000
a=$( { time ping $1 -c 4; } 2>&1 |grep "real" | awk '{print $2}' | awk -F m '{print $1$2}' | awk -F s '{print $1}' | awk -F . '{print $1$2}' )
echo " "
if [ "$a" -gt "$ref" ]; then 
 echo "Ddos Detected"
else 
 echo "Server is Up and Running"
fi
