#!/bin/bash


echo " Press Option <1-9> To Check System Logs "
echo
echo "1 = Check Failed Login Attempt For User "
echo "2 = Check All Users Failed Login Attempt "
echo "3 = To Lock User Account After Failed Login "
echo "4 = To Lock Root Account After Failed Login "
echo "5 = Set Maximum Number of Login Failures For User "
echo "6 = Set Maximum Number of Login Failures For Root "
echo "7 = Reset The Counters Of Login Failures"
echo "8 = To Reset Counter For User"
echo "9 = Exit"
echo
read NUM
if [ "$NUM" -eq 1 ]; then 
echo " Failed Login Attempt For User : "
echo "Enter User Name :"
read root
faillog -u $root
elif [ "$NUM" -eq 2 ]; then
echo "All Users Failed Login Attempt :"
faillog -a
elif [ "$NUM" -eq 3 ]; then 
echo " Lock User Account After Failed Login : "
echo "Enter User Name : "
read usr
echo "Enter Time In Seconds :"
read sec
faillog -l $sec -u $usr
elif [ "$NUM" -eq 4 ]; then
echo "Lock Root Account After Failed Login :"
echo "Enter Time In Seconds :"
read ro
faillog -l $ro
elif [ "$NUM" -eq 5 ]; then
echo " Maximum Number of Login Failures For User Accounts : "
echo "Enter Max Num Count Attempts : "
read d
echo "Enter User Name :"
read u
faillog -M $d -u $u
elif [ "$NUM" -eq 6 ]; then
echo " Maximum Number of Login Failures For Root Accounts :"
echo "Enter Max Num Count Attempts : "
read f
faillog -M $f
elif [ "$NUM" -eq 7 ]; then
echo "Reset The Counters Of Login Failures : "
faillog -r
elif [ "$NUM" -eq 8 ]; then
echo "To Reset Counter For User :"
echo "Enter User Name : "
read v
faillog -r -u $v
elif [ "$NUM" -eq 9 ]; then
exit 0
else " Invalid Option : "
exit 0
fi

