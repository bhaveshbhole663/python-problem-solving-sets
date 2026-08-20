# Write a program to print multiplication table of a given number using for loop.
# A By while loop
Number = int(input("Enter your number for which you want multiplication table: "))

i = 1

while i<11:
    print(Number,"X",i,"=",Number*i)
    i+=1


# B By for loop 

n = int(input("Enter a number: "))

for  i in range(1, 11):
    print(f"{n} X {i} = {n*i}")