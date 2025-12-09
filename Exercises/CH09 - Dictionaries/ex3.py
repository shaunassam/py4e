###########################
## CHAPTER 9: EXERCISE 3 ##
###########################
# Write a program to read through a mail log, build a histogram using
# a dictionary to count how many messages from come from each email
# address, and print the dictionary.

count = 0
emaildict = dict()
email = None

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = 'mbox-short.txt'
else:
    print("Cannot find filename")
fhand = open(fname)

for line in fhand:
    line = line.strip()
    if line.startswith("From"):
        if line.startswith("From:"):
            continue
        else:
            line = line.rsplit()
            email = line[1]
            if email not in emaildict:
                emaildict[email] = 1
            else:
                emaildict[email] += 1
print(emaildict)