# Rewrite grade program using a function called computegrade that takes a score as its parameter and returns a grade as a string.

def computegrade(x):
    if x >= 0.9 and x <= 1.0:
        return 'A'
    elif x >= 0.8 and x < 0.9:
        return 'B'
    elif x >= 0.7 and x < 0.8:
        return 'C'
    elif x >= 0.6 and x < 0.7:
        return 'D'
    elif x < 0.6 and x >= 0.0:
        return 'F'
    else:
        return 'Bad score. Enter a number between 0.0 and 1.0'

try:
    score = input("Enter score: ")
    flscore = float(score)
    print(computegrade(flscore))

except:
    print("Bad score")