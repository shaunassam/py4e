############################
## CHAPTER 11: EXERCISE 1 ##
############################
# Write a simple program to simulate the operation of the grep 
# command on Unix. Ask the user to enter a regular expression 
# and count the number of lines that matched the regular expression.

import re

counter = 0

usrreinp = input("Enter a regular expression: ")

if len(usrreinp) < 1:
    print("Invalid entry.")
    quit()
else:
    fhand = open("mbox.txt")

    for line in fhand:
        line = line.rstrip()
        check = re.search(usrreinp, line)
        if check is not None:
            counter += 1
        else:
            continue

    print("mbox.txt had", counter, "lines that matched", usrreinp)