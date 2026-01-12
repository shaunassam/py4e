###########################
## CHAPTER 9: EXERCISE 2 ##
###########################
# Write a program that categorizes each mail message by
# which day of the week the commit was done. Look for lines
# that start with 'From', then look for the third word and
# keep a running count of each of the days of the week. At
# the end the program should print out the contents of the
# dictionary.

count = 0
dictday = dict()
weekday = None

fhand = open('mbox-short.txt')

for line in fhand:
    line.split()
    if line.startswith("From"):
        if line.startswith("From:"):
            continue
        else:
            line = line.strip()
            linespace = line.find(" ")
            lenline = len(line)
            removefrom = line[linespace+1:lenline]
            removefrom = removefrom.split()
            weekday = removefrom[1]
            if weekday not in dictday:
                dictday[weekday] = 1
            else:
                dictday[weekday] += 1
print(dictday)