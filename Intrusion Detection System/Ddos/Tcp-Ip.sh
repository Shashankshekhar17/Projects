#!/bin/bash

echo "Checking For TCP/IP Denial of Service Attack:"
while :
do
check=$(netstat -ntu | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -n|wc -l)
if  [ $check -gt 20 ]
then
echo "$(tput bold)$(tput setaf 1)"
echo "[-] TCP/IP Denial of Service Attack In Progress-------------------OK"
else
echo "[+] TCP/IP Denial of Service Attack NOT in Progress-------------------OK"
fi
sleep 3s
done
