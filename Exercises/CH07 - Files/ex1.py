###########################
## CHAPTER 7: EXERCISE 1 ##
###########################
# Write a program to read through the `mbox-short.txt` file
# and print the contents line by line all in upper case.
# File downloaded from: https://www.py4e.com/code3/mbox-short.txt

fileinp = input("Enter a file name: ")
fopen = open(fileinp)
for line in fopen:
    line = line.rstrip()
    print(line.upper())