#!/bin/bash


echo "Your current MAC address for the default gateway is:"
echo

# Determine default gateway IP address
ip=$(netstat -rn | grep 0.0.0.0 | awk '{print $2}' | grep --invert-match "0.0.0.0" --max-count=1)
 
# Determine original default gateway MAC address by using found IP address
original_mac=$(arp -a $ip | awk '{print $4}')

echo Current MAC Address----------------------------------------------: $original_mac 
echo Default Gateway IP Address---------------------------------------: $ip

echo
 
while :
do
        # Determine current default gateway IP address
        ip=$(netstat -rn | grep 0.0.0.0 | awk '{print $2}' | grep --invert-match "0.0.0.0" --max-count=1)
       
        # Determine current default gateway MAC address by using found IP address
        current_mac=$(arp -a $ip | awk '{print $4}')
       
        # Compare the two MAC addresses
        if [ $original_mac == $current_mac ]
                then
                        # If both match
                        echo "[+] ARP Poisoning NOT In Progress-------------------OK"
                else
                        # If both do not match get IP address sending ARP broadcasts
                        current_ip=$(arp -v | grep $current_mac --max-count=1 | awk '{print $1}')
                        echo "$(tput bold)$(tput setaf 1)"
                        echo "[-] Alert! MAC ADDRESS CHANGE DETECTED ARP Poisoning In Progress.......!!!!"
                        echo "    Suspect MAC: $current_mac"
                        echo "    Suspect IP: $current_ip $(tput sgr0)"
        fi
        sleep 5s
done
