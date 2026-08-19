# Write a program to find out whether a student has passed or failed if it requires a total of
#40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an
#input from the user

sub1_marks = float(input("Enter sub1 marks: "))
sub2_marks = float(input("Enter sub2 marks: "))
sub3_marks = float(input("Enter sub3 marks: "))
total = sub1_marks+sub2_marks+sub3_marks
percentage = (total/300)*100

if(sub1_marks>=33 and sub2_marks >= 33 and sub3_marks >= 33 and percentage >=40):
    print("Passed")

else:
    print("Failed")

print("Perentage",percentage,"%")
