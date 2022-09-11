#!/bin/bash

echo " Press Option <1-7> To Check System Logs "
echo
echo "1 = Last Login Time "
echo "2 = Last Boot Time "
echo "3 = Last Reboot Time "
echo "4 = Last Shutdown Time "
echo "5 = Full Reboot Report"
echo "6 = Full Shutdown Report"
echo "7 = Exit"
echo
read NUM
if [ "$NUM" -eq 1 ]; then 
echo " Last Login is : "
last login
elif [ "$NUM" -eq 2 ]; then
echo "Last Boot Time is :"
who -b
elif [ "$NUM" -eq 3 ]; then 
echo " Last Reboot Time is : "
last reboot | head -1
elif [ "$NUM" -eq 4 ]; then
echo "Last Shutdown Time is :"
last -x | grep shutdown | head -1
elif [ "$NUM" -eq 5 ]; then
echo " Full Reboot Report is : "
last reboot
elif [ "$NUM" -eq 6 ]; then
echo " Full Shutdown Report is :"
last -x | grep shutdown
elif [ "$NUM" -eq 7 ]; then
exit 0
else " Invalid Option : "
exit 0
fi

