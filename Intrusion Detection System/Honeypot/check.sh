#!/bin/bash

#sleep 20s
Init_size=$(stat -c %s /root/Desktop/ids/Honeypot/HoneypotLog/Port_Attack_Scan | awk '{print $1}')
echo
while :
do
Curr_size=$(stat -c %s /root/Desktop/ids/Honeypot/HoneypotLog/Port_Attack_Scan | awk '{print $1}')
ip=$(cat /root/Desktop/ids/Honeypot/HoneypotLog/Port_Attack_Scan | awk '{print $2}' | sort -u)
if [ $Curr_size != $Init_size ]
then
echo "$(tput bold)$(tput setaf 1)"
echo "[-] Alert ! Scanning In Progress.......................OK"
echo "Suspect IP : $ip $(tput sgr0)"
else
echo "[+] Scanning NOT In Progress-------------------OK"
fi
sleep 3s
done
