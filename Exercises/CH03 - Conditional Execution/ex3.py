# Chapter 3 - Exercise 3
# Write program to prompt for score between 0.0 and 1.0.
# If out of range print error.
# A: >= 0.9, B: >= 0.8, C: >= 0.7, D: >= 0.6, F: < 0.6

score = input("Enter score: ")

try:
    fscore = float(score)
    if fscore >= 0.9 and fscore <= 1.0:
        print("A")
    elif fscore >= 0.8 and fscore < 0.9:
        print("B")
    elif fscore >= 0.7 and fscore < 0.8:
        print("C")
    elif fscore >= 0.6 and fscore < 0.7:
        print("D")
    elif fscore < 0.6 and fscore >= 0.0:
        print("F")
    else:
        print("Bad score. Enter a score between 0.0 and 1.0")
except:
    print("Bad score. Enter a number between 0.0 and 1.0")
    exit(1)