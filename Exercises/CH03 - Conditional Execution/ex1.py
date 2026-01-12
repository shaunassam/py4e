# Chapter 3 - Exercise 1
# Rewrite pay computation to give employee 1.5x hourly rate for hours worked over 40 hours.

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
flhours = float(hours)
flrate = float(rate)

if flhours > 40:
    othours = flhours - 40
    pay = ((flrate * 1.5) * othours) + (flrate * 40)
    print(pay)
else:
    pay = flhours * flrate
    print(pay)