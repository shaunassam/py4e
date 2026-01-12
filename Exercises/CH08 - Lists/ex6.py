###########################
## CHAPTER 8: EXERCISE 6 ##
###########################
# Rewrite the program prompting the user for a list of numbers
# and prints out the max and min at the end when the user
# enters 'done'. Store the numbers in a list and use the 
# `max()` and `min()` functions.

endme = False
numlist = list()

while endme is False:
    userinp = input("Enter a number: ")
    if userinp == 'done':
        endme = True
        if not numlist:
            quit()
    else:
        try:
            intval = int(userinp)
            numlist.append(intval)
        except:
            print("Invalid entry. Enter a number or type 'done' to exit.")
maxlist = max(numlist)
minlist = min(numlist)
print("Maximum:", maxlist)
print("Minimum:", minlist)