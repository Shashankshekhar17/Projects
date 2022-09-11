#!/bin/bash


echo "loading..."
sleep 15s
Init_pro=$(ps -a | grep tcpdump --count)
echo
while :
do
Curr_pro=$(ps -a | grep tcpdump --count)
if [ $Init_pro == $Curr_pro ]
then
echo "[+] Flooding NOT In Progress-------------------OK"
else
echo "$(tput bold)$(tput setaf 1)"
echo "[-] Flooding In Progress.......................OK"
fi
sleep 3s
done
