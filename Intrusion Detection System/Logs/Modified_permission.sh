#!/bin/bash

FILE="$1"

# make sure we got file-name as command line argument

if [ $# -eq 0 ]
then
echo "Usage :"
echo "$0 <Give Full Path of File or Direcory>"
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
    
echo "Permission of file : $(ls -l $FILE)"
echo "SELinux security context string : $(stat -c %C $FILE)"
echo "Number of hard links : $(stat -c %h $FILE)"

