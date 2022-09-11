#!/bin/bash


echo "Enter Your Network Interface :"
read fa
echo
echo "Enter Port You Want To Check <0-65000> :"
read po
echo
tcpdump -c 10 -i $fa port $po
