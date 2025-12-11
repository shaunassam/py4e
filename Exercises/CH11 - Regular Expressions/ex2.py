############################
## CHAPTER 11: EXERCISE 2 ##
############################
# Write a program to look for lines of the form: `New Revision: 39772`
# Extract the number from each of the lines using a regular expression 
# and the findall() method. Compute the average of the numbers and print 
# out the average as an integer

import re

count = 0
totalsum = 0

fhand = open("mbox.txt")

for line in fhand:
    line = line.rstrip()
    numextract = re.findall('^New.*:\\s([0-9].*$)', line)
    if len(numextract) > 0:
        numextract = numextract[0]
        intnum = int(numextract)
        totalsum += intnum
        count += 1
avg = totalsum / count
print(int(avg))