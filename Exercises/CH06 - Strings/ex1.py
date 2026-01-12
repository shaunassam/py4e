###########################
## CHAPTER 6: Exercise 1 ##
###########################
# Write a while loop that starts at the last character of a string and
# works its way backwards to the first character, printing each letter
# on a separate line.

word = input("Enter a word: ")
count = len(word)
while count > 0:
    print(word[count - 1])
    count = count - 1