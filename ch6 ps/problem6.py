# Write a program to calculate the grade of student from his marks from the following scheme
# 90-100 => Ex  80-90=>A    70-80=>B   60-70=>C   50-60=>D    <50=>F

m1 = int(input("Enter marks in sub 1: "))
m2 = int(input("Enter marks in sub 2: "))
m3 = int(input("Enter marks in sub 3: "))
m4 = int(input("Enter marks in sub 4: "))
m5 = int(input("Enter marks in sub 5: "))

total = m1+m2+m3+m4+m5
percentage = (total/500)*100

if(percentage>90 and percentage<=100):
    print("Your Grade is : Ex",percentage)

elif(percentage>80 and percentage<=90):
    print("Your Grade is : A",percentage)

elif(percentage>70 and percentage<=80):
    print("Your Grade is : B",percentage)

elif(percentage>60 and percentage<=70):
    print("Your Grade is : C",percentage)

elif(percentage>50 and percentage<=60):
    print("Your Grade is : D",percentage)

else:
    print("Your Grade is : F",percentage)


                 