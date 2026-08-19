# Write a program to find whether a given username contains less than 10 characters or not.

username = input("Enter your user name: ")

length = len(username)

if(length<10):
    print("This username has less than 10 characters")

else:
    print("This username has more than or equal to 10 characters")