## Chapter 2 - Exercise 5
## Program which prompts user for Celsius and converts temperature to Fahrenheit

inpCelsius = input("Enter the temperature in Celsius: ")

# Formula: (0°C × 9/5) + 32 = 32°F
fahrenheit = (float(inpCelsius) * (9/5)) + 32
print(fahrenheit)