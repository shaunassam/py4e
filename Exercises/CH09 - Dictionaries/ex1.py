###########################
## CHAPTER 9: EXERCISE 1 ##
###########################
# Write a program that reads the words in 'words.txt' and stores
# them as keys in a dictionary. It doesn't matter what the values
# are. Then use the `in` operator as a fast way to check whether
# a string is in the dictionary.

wordlist = dict()
count = 0

fhand = open('words.txt')
for line in fhand:
    line = line.split()
    for word in line:
        count = count + 1
        wordlist[word] = count
print(wordlist)
checkword = input("Enter a word to check the word list: ")
if checkword in wordlist:
    print(checkword, wordlist.get(checkword, 0))
else:
    print(checkword, "is not in the word list.")