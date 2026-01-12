# Rewrite pay computation program — with 1.5x for overtime — using a function called "computepay".

def computepay(hrs, rt):
    if hrs > 40:
        othrs = hrs - 40
        otpay = othrs * (rt * 1.5)
        pay = (40 * rt) + otpay
        return pay
    else:
        pay = hrs * rt
        return pay
    
hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
flhours = float(hours)
flrate = float(rate)
print(computepay(flhours, flrate))