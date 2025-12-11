############################
## CHAPTER 11: EXERCISE X ##
############################
#################################
# THIS IS THE ONLINE ASSIGNMENT #
#################################
# Write a program to read through and parse a file with text and numbers.
# Extract all the numbers in the file and compute the sum of the numbers.
# Sample data from: `regex_sum_42.txt` contains 90 values with a sum=445833
# Actual data from: `regex_sum_2335783.txt` contains 82 values and the sum ends with 780

import re

sumnum = 0

fhand = open("regex_sum_2335783.txt")

for line in fhand:
    line = line.rstrip()
    foundnum = re.findall('([0-9]+)', line)
    if len(foundnum) < 1:
        continue
    else:
        for i in foundnum:
            inti = int(i)
            sumnum += inti
print(sumnum)
