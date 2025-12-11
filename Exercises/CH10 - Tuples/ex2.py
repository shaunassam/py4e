############################
## CHAPTER 10: EXERCISE 2 ##
############################
# This program counts the distribution of the hour of the day
# for each of the messages. You can pull the hour from the 'From'
# line by finding the time string and splitting it from the colon
# character. Once the counts of the hours have been accumulated,
# print out the counts, one per line, sorted by hour.

lsthours = list()
dicthours = dict()

fname = input("Enter a file name: ")
try:
    fhand = open(fname)
except:
    print("Invalid file name")
    quit()

for line in fhand:
    if line.startswith("From"):
        if line.startswith("From:"):
            continue
        else:
            line = line.split()
            time = line[5]
            timesplit = time.find(":")
            timehour = time[:timesplit]
            if timehour not in dicthours:
                dicthours[timehour] = 1
            else:
                dicthours[timehour] += 1

for (k, v) in dicthours.items():
    lsthours.append((k, v))

lsthours.sort()

for (k, v) in lsthours[:]:
    print(k, v)