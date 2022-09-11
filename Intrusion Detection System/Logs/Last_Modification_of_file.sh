#!/bin/bash

FILE="$1"

# make sure we got file-name as command line argument

if [ $# -eq 0 ]
then
echo "Usage :"
echo "$0 <Give Full Path of File>"
exit 1
fi
  
which stat > /dev/null
     
# make sure stat command is installed

if [ $? -eq 1 ]
then
echo "stat command not found!"
exit 2
fi
     
# make sure file exists

if [ ! -e $FILE ]
then
echo "$FILE not a file"
exit 3
fi
     
# use stat command to get info
    
echo "Time of last access : $(stat -c %x $FILE)"
echo "Time of last modification : $(stat -c %y $FILE)"
echo "Time of last change : $(stat -c %z $FILE)"
