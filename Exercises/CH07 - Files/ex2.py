###########################
## CHAPTER 7: EXERCISE 2 ##
###########################
# Write a program to prompt for a file name and read through the file
# searching for lines of the form `X-DSPAM-Confidence: 0.8475`.
# For each 'X-DSPAM-Confidence' line found, extract the floating-point number.
# Count the lines and compute the total of those values, then print out the
# average spam confidence.

count = 0
xdspam = 0
file = input("Enter the file name: ")

try:
    fopen = open(file)
except:
    print("File", file, "not found.")
    quit()

for line in fopen:
    if line.startswith("X-DSPAM-Confidence"):
        strlen = len(line)
        colonpos = line.find(":")
        val = line[colonpos+1:strlen]
        flval = float(val)
        xdspam = xdspam + flval
        count = count + 1
avgconfidence = xdspam / float(count)
print("Average spam confidence:", avgconfidence)