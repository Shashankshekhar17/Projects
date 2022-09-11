#!/bin/bash


echo "--------------------------------------------------------------"
echo ">>----------------AVAILABLE INTERFACE LIST------------------<<"
echo "--------------------------------------------------------------"
echo ""
cat /tmp/ethlist
echo ""
echo "--------------------------------------------------------------"
echo ""
echo "You Got 120 Second To Fill The Interface Name Or It Will Start Automatically"
xterm -hold -e sh /root/Desktop/ids/Honeypot/Port_Scan_attack_Detect.sh | xterm -hold -e sh /root/Desktop/ids/Honeypot/check.sh


