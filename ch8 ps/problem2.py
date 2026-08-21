# Write a python program using function to convert Celsius to Fahrenheit
# f = c*(9/5)+32

def convertor():
    celcius = int(input("Enter the temperature in celcius: "))
    fahrenheit = celcius*(9/5)+32
    print(f"The temperature in fahrenheit is {fahrenheit}")

convertor()

def convertor():
    f = int(input("Enter the temperature in fahrenheit: "))
    c = 5*(f-32)/9
    print(f"The temperature in celcius is {round(c,2)}")    # this round function is for rounding off the decimalis 

convertor()

