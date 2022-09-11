#!/bin/bash


echo "Enter Your Network Interface :"
read fa
echo
echo
tshark -i $fa -f "ip proto 6 or ip proto 17" -R "tcp.flags == 16 or tcp.flags == 1 or tcp.flags == 2 or tcp.flags == 18 or tcp.flags == 41 or tcp.flags == 16 or tcp.flags == 0 or ip.len == 28 or icmp.type == 8" >> /root/Desktop/ids/Honeypot/HoneypotLog/Port_Attack_Scan

