#  To accept marks of 6 students and display them in a sorted manner
marks = []

S1 = int(input("Enter s1 marks here : "))
marks.append(S1)
S2 = int(input("Enter s2 marks here : "))
marks.append(S2)
S3 = int(input("Enter s3 marks here : "))
marks.append(S3)
S4 = int(input("Enter s4 marks here : "))
marks.append(S4)
S5 = int(input("Enter s5 marks here : "))
marks.append(S5)
S6 = int(input("Enter s6 marks here : "))
marks.append(S6)

marks.sort()
print(marks)