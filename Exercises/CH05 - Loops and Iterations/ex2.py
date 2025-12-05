# Write another program that prompts for a list of numbers as in EXERCISE 1 and at the end prints
# out both the maximum and minimum of the numbers instead of the average.

goodbye = False
sum = 0
count = 0
max = None
min = None

while goodbye is False:
    userinp = input("Enter a number [enter 'done' to exit]: ")
    if userinp != "done":
        try : 
            intinp = int(userinp)
            if max is None:
                max = intinp
            elif intinp > max:
                max = intinp
            if min is None:
                min = intinp
            elif intinp < min:
                min = intinp
            sum = sum + intinp
            count = count + 1
            print(count, "|", intinp)
        except:
            print("Invalid entry. Enter a number or 'done' to exit.")
    else :
        goodbye = True

print("Total:", sum)
print("Count:", count)
print("Max:", max, "|", "Min:", min)