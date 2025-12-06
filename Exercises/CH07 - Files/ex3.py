###########################
## CHAPTER 7: EXERCISE 3 ##
###########################
# Add an Easter Egg. Create a program that counts the number of
# 'Subject' lines in the file. If the user enters "na na na boo boo"
# output a funny message.

count = 0

fileinp = input("Enter a file name: ")
if fileinp.lower() == "na na na boo boo":
    print("NA NA NA BOO BOO TO YOU — You have been punk'd!")
    quit()
else:
    try:
        fopen = open(fileinp)
    except:
        print("Bad file name.")
        quit()

for line in fopen:
    if line.startswith("Subject"):
        count = count + 1

print("There were", count, "subject lines in", fileinp)