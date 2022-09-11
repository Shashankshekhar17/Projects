#!/bin/bash


echo "Checking For Ping Of Death Attack :"
echo ""
echo "[+] Loading Sniffer             [Ok]"
echo ""
sleep 5s
echo "[+] Your Result Will Be Up In 20 Seconds."
echo ""
sleep 3s
echo "[+] Sniffing Started            [OK]"
echo ""
tshark -i wlan0 -R "icmp.type == 8" -c 200 >> /root/Desktop/ids/Ddos/DdosLogs/ping_of_death
echo ""
echo "[+] Sniffing Finished           [OK]"
echo ""
echo "[+] Loading Result              [OK]"
sleep 3s
echo "----------------------------------------------------------------------------------"
echo ">>-------------IP-Address Of Device Performing Ping Of Death Are------------------<<"
echo "----------------------------------------------------------------------------------"
echo ""
cat /root/Desktop/ids/Ddos/DdosLogs/ping_of_death | awk '{print $2}' | sort -u
echo ""
