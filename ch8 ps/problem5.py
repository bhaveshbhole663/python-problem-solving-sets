'''
Write a python function to print first n lines of the following pattern.
***
**      for n=3
*
'''

def fun1():
    i = 1
    for i in range(1,4):
        print("*"*(4-i), end="")
        print("")

fun1()
