#Write a program to find the greatest of four numbers entered by the user

number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))
number3 = int(input("Enter number 3: "))
number4 = int(input("Enter number 4: "))

if(number1>number2 and number1>number3 and number1>number4):
    print("Number1 is greatest among all")

elif(number2>number1 and number2>number3 and number2>number4):
    print("Number2 is greatest among all")
    
elif(number3>number1 and number3>number2 and number3>number4):
    print("Number3 is greatest among all")

else:
    print("Number4 is greatest among all")
    