# Write a program using functions to find greatest of three numbers


def fun():
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))

    if(a>b and a>c):
        print(f"The greatest number among these three is {a}")
    elif(b>a and b>c):
        print(f"The greatest number among these three is {b}")
    elif(c>b and c>a):
        print(f"The greatest number among these three is {c}")

fun()