#!/bin/bash


echo "Checking For Establish Connection Denial of Service Attack:"
check=$(lsof -i TCP:80 |wc -l)
while :
do
if  [ $check -gt 20 ]
then
echo "$(tput bold)$(tput setaf 1)"
echo "[-] ESTABLISHED CONNECTIONS Attack In Progress-------------------OK"
else
echo "[+] ESTABLISHED CONNECTIONS Attack NOT in Progress-------------------OK"
fi
sleep 3s
done
