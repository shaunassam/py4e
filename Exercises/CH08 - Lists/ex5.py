###########################
## CHAPTER 8: EXERCISE 5 ##
###########################
# Write a program to read through the mail box data and
# when you find a line that starts with 'From:' split the
# line into words using `split` function and print who
# sent the message. Also print a count at the end.

count = 0
myfile = input("Enter a file name: ")
fhand = open(myfile)

for line in fhand:
    line.split()
    if line.startswith('From:'):
        colonpos = line.find(':')
        linelen = len(line)
        email = line[colonpos+1:linelen]
        print(email.strip())
        count = count + 1
print("There were", count, "lines in the file with From as the first word")