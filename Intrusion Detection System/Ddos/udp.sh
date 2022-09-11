#!/bin/bash

echo "Checking For UDP Denial of Service Attack:"
while :
do
check=$(netstat -anp | grep 'udp' | wc -l)
if  [ $check -gt 20 ]
then
echo "$(tput bold)$(tput setaf 1)"
echo "[-] UDP Flooding In Progress-------------------OK"
else
echo "[+] UDP Flooding NOT in Progress-------------------OK"
fi
sleep 3s
done

