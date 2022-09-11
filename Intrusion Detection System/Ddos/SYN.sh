#!/bin/bash


echo "Checking For SYN Denial of Service Attack:"
while :
do
check=$(netstat -nap | grep SYN | wc -l)
if  [ $check -gt 20 ]
then
echo "$(tput bold)$(tput setaf 1)"
echo "[-] SYN Flood Attack In Progress-------------------OK"
else
echo "[+] SYN Flood Attack NOT in Progress-------------------OK"
fi
sleep 3s
done
