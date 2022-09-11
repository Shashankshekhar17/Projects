#!/bin/bash


FILE="$1"

# make sure we got file-name as command line argument

if [ $# -eq 0 ]
then
echo "Usage :"
echo "$0 <Give Full Path of File or Directory>"
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
    
echo "Inode Numbe Of File : $(stat -c %i $FILE)"
echo "Input/Output Block Size : $(stat -c %o $FILE)"
echo "Total Size in Bytes : $(stat -c %s $FILE)"
echo "Fundamental block size (for block counts) : $(stat -c %S $FILE)"
echo "Number of blocks allocated : $(stat -c %c $FILE)"



