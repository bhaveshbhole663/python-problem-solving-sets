# Write a recursive function to calculate the sum of first n natural numbers
n = int(input("Enter the number you want sum upto :"))
def recfun(n):
    if(n==1):
        return 1
    else:
        return  n + recfun(n-1) 

sum = recfun(n)
print(sum)

