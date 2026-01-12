# Write a program which repeatedly reads integers until the user enters “done”.
# Once “done” is entered, print out the total, count, and average of the integers.
# If the user enters anything other than an integer, detect their mistake using try 
# and except and print an error message and skip to the next integers.

goodbye = False
sum = 0
count = 0

while goodbye is False:
    numinput = input("Enter a number [or 'done' to exit]: ")
    if numinput != "done":
        try: 
            intnum = int(numinput)
            print((count + 1), "|", intnum)
            sum = sum + intnum
            count = count + 1
        except:
            print(numinput, "is an invalid entry. Enter only numbers.")
    else:
        goodbye = True

print("Total sum:", sum)
print("Total count:", count)
print("Average total:", float(sum/count))