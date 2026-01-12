############################
## CHAPTER 10: EXERCISE 1 ##
############################
# Read and parse 'From' lines and pull out the address from the line.
# Count the number of messages from each person using a dictionary.
# After all the data has been read, print the person with the most
# commits by creating a list of (count, email) tuples from the dictionary.
# Then sort the list in reverse order and print out the person with the
# most commits.

tuplist = list()
emailcnt = dict()

fname = input("Enter a file name: ")
try:
    fhand = open(fname)
except:
    print("Invalid file name.")
    quit()

for line in fhand:
    if line.startswith("From"):
        if line.startswith("From:"):
            continue
        else:
            line = line.split()
            email = line[1]
            if email not in emailcnt:
                emailcnt[email] = 1
            else:
                emailcnt[email] += 1

for (k, v) in emailcnt.items():
    tuplist.append((v, k))

tuplist.sort(reverse=True)

for key, val in tuplist[:1]:
    print(key, val)