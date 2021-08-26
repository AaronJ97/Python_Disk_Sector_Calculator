#HDD Sector Calculator 2021
#Programming portfolio piece by AaronJ97 GitHub

#for help and support on this script please goto:
# https://www.github.com/AaronJ97 

# Make a program which calculates the amount of sectors in a given storage
# drive.

# The program takes an input from the user declaring the disk size
# of the drive they wish to calculate the sectors of. 

#The program first takes the disk size-input (string by default) and converts to 
# an integer to be used for calculation.

#The disk size is then converted from Gigabytes (GB) to Bytes using a simple
# equation.  DiskSize(bytes) = diskSize(GB)*1024*1024*1024
#There are 512 bytes per sector so we can use that to work out how many
# sectors there are. This can be achieved by
# dividing the disk size in bytes by the sector size in bytes.

#once the script runs its calculation it prints the relevant data on
# to the screen.