###########################
## CHAPTER 9: EXERCISE 4 ##
###########################
# Add code to the program in CH09 > ex4 to figure out
# who sent the most messages in the file. After dictionary
# has been made, look through it using a maximum loop to find
# who sent the most messages and print how many messages the
# person has.

emaildict = dict()
email = None
maxim = None

fhand = open('mbox-short.txt')

for line in fhand:
    if line.startswith("From"):
        if line.startswith("From:"):
            continue
        else:
            line = line.split()
            email = line[1]
            if email not in emaildict:
                emaildict[email] = 1
            else:
                emaildict[email] += 1

for key in emaildict:
    if maxim is None:
        maxim = emaildict[key]
    elif emaildict[key] > maxim:
        maxim = emaildict[key]

for key, value in emaildict.items():
    if value == maxim:
        print(key, value)