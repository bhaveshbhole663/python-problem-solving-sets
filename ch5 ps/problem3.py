#we have to check whether set can contain int 18 and str 18 

s = set()

a = 18
s.add(a)

b = "18"
s.add(b)

print(s)

# both str and int is printed in set so it is possible that set contains both int and str  
