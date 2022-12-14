#!/bin/bash

# Stop networking
stopNetworking () {
    service networking stop > /dev/null 2>&1
}

stopMonitor () {
    echo -n "Stopping monitor device...           "
    airmon-ng stop mon0 > /dev/null 2>&1
    airmon-ng stop mon1 > /dev/null 2>&1
    airmon-ng stop mon2 > /dev/null 2>&1
    sleep 2
    echo "DONE"
}

# Stop the fake access point
killAP () {
    echo -n "Shutting down the fake AP...         "
    basepid=`ps -ef | grep -i [a]irbase | awk '{ print $2 }'`
    kill -9 $basepid > /dev/null 2>&1
    echo "DONE"
}

# Kill all external access
killExternalAccess () {
    echo -n "Killing external access...           "
    ifconfig at0 down > /dev/null 2>&1
    sleep 2 
    echo "DONE"
}

# Stop the DHCP server
stopDHCP () {
    echo -n "Stopping DHCP server...              "
    service dhcp3-server stop > /dev/null 2>&1
    sleep 2 
    echo "DONE"
}

# Kill routing and forwarding
noRouteAPClients () {
    echo -n "Killing routing...                   "
    iptables -t nat -D POSTROUTING -o wlan0 -s 192.168.121.0/24 -j MASQUERADE > /dev/null 2>&1
    echo 0 > /proc/sys/net/ipv4/ip_forward
    echo "DONE"
}

# Kill any logs or captures that were generated
killLogs () {
    echo -n "Killing logs...                      "
    rm -f /tmp/ap_access_list > /dev/null 2>&1
    rm -f /tmp/ethlist > /dev/null 2>&1
    rm -Rf /tmp/driftimages > /dev/null 2>&1
    rm -f /tmp/pre > /dev/null 2>&1
    rm -f /tmp/post > /dev/null 2>&1
    echo "DONE"
}
# Main Execution
clear
echo "        Clean Killing Everything..."
echo "------------------------------------------"
echo 
noRouteAPClients
stopDHCP
killExternalAccess
killAP
stopMonitor
stopNetworking
killLogs

echo 
echo "--------------------------------------------"
echo
echo "Shutdown complete!"
echo
