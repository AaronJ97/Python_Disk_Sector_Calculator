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

#the script is kept inside a function, so that it continues to run
# after the first calculation (meaning it wont just exit allowing
# you to perform more calculations rather than just one before having to
# reopen the program). Also the function calling itself stops the program
# randomly quitting before an input is made.
def HARD_DISK_CALCULATOR():

    #input from user stored as variable HDC -Hard Disk Capacity
    HDC = input("HARD_DISK_CAPACITY: ")

    #the previous input is stored in a new variable (to prevent crashing)
    #and is converted into an integer using int(variable)
    hard_disk_capacity = int(HDC)

    #Once the HDC is converted to integer (because by default an input is 
    # a string)it can now be used in the calculation. first off convert
    # from GB to bytes. 
    hard_disk_capacity_bytes = hard_disk_capacity *1024 *1024 *1024

    #sector size constant used during the sector amount calculation declares
    #how large a sector is in bytes.
    disk_sector_size_bytes = 512

    #the converted HDC (hard_disk_capacity_bytes) can now be divided 
    # by the total of bytes per sector to give us the total number of 
    #sectors and stores it inside the variable sector_amount
    sector_amount = hard_disk_capacity_bytes // disk_sector_size_bytes

    #using the variables and data from the calculation the program
    #now converts the integers to strings to be used in string 
    #concatenation for the purpose of displaying output to the screen
    #showing the relevant data.
    print("HARD DISK SIZE: " + str(hard_disk_capacity) + " GB")
    print("DISK SECTOR SIZE: " + str(disk_sector_size_bytes) + " BYTES")
    print("HARD DISK CAPACITY: " + str(hard_disk_capacity_bytes) + " BYTES")
    print("TOTAL SECTORS ON DISK: " + str(sector_amount) + " SECTORS")

    #function name called within itself so the calculator can be used again
    #and again without quitting and needing to be re-opened.
    HARD_DISK_CALCULATOR()

#function calls itself to begin with so that the program actually opens.
HARD_DISK_CALCULATOR()
