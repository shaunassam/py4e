# Chapter 3 - Exercise 2
# Rewrite excercise 1 computation using try/except to handle non-numeric input.

hours = input("Enter Hours: ")
try:
    fhours = float(hours)
except:
    print("Error, please enter numeric input")
    exit(1)

rate = input("Enter Rate: ")
try:
    frate = float(rate)
    pay = fhours * frate
    print("Pay:", pay)
except:
    print("Error, please enter numeric input")
    exit(1)