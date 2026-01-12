############################
## CHAPTER 10: EXERCISE 3 ##
############################
# Write a program that reads a file and prints the letters in
# decreasing order of frequency. It should convert all the input into
# lower case and only count the letters a-z. The program should
# not count spaces, digits, punctuation, or anything other than
# the letters a-z.

dictletr = dict()
lstletr = list()

fname = input("Enter a file name: ")
try:
    myfile = open(fname)
except:
    print("Could not find the file.")
    quit()

for line in myfile:
    line.strip()
    for letter in line:
        if letter.isalpha():
            letter = letter.lower()
            dictletr[letter] = dictletr.get(letter,0) + 1
        else:
            continue

for (ltr, val) in dictletr.items():
    lstletr.append((val, ltr))

lstletr.sort(reverse=True)
for (v, l) in lstletr[:]:
    print(l, v)