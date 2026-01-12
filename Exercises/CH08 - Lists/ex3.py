###########################
## CHAPTER 8: EXERCISE 3 ##
###########################
# Rewrite the following program to condense the
# two `if` statements into one.
###
# fhand = open('mbox-short.txt')
# count = 0
# for line in fhand:
#     words = line.split()
#     # print('Debug:', words)
#     if len(words) == 0 : continue
#     if words[0] != 'From' : continue
#     print(words[2])
###

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    if len(words) == 0 or words[0] != 'From':
        continue
    print(words[2])