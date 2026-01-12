###########################
## CHAPTER 6: EXERCISE 3 ##
###########################
# Create a function named "count" that accepts the string and letter
# as arguments and output's the count of a letter in the word.

def count(wrd, altr):
    count = 0
    for ltr in wrd:
        if ltr == altr:
            count = count + 1
    return count

word = "banana"
letter = "a"
acnt = count(word, letter)
print("The letter", letter, "appears", acnt, "times in the word:", word)