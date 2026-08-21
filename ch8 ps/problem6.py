#  Write a python function which converts inches to cms

def convertor():
    inch = int(input("Enter the length in inch: "))
    cms = inch/2.54
    return cms

answer = convertor()
print("Length in cm is",answer)
