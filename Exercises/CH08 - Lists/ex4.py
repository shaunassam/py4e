###########################
## CHAPTER 8: EXERCISE 4 ##
###########################
# Write a program listing all unique words in the
# 'romeo.txt' file and sort them alphabetically.

newlist = list()

fhand = open('romeo.txt')
for line in fhand:
    words = line.split()
    for word in words:
        if word in newlist:
            continue
        else:
            newlist.append(word)
newlist.sort()
print(newlist)
