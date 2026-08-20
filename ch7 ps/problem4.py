# Write a program to find whether a given number is prime or not.
#By for loop
n = int(input("Enter your number: "))

for i in range(2, n):
    if(n%i)==0:
        print("This number is not a prime number")
        break
else:
    print("Number is prime")

#By while loop

n = int(input("Enter your number: "))

i = 2
while i<n:
    if(n%i)==0:
        print("It is not prime number ")
        break
    i+=1
else:
    print("It is a prime number")