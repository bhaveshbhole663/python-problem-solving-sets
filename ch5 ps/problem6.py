# To create empty dict allow 4 friends to enter their fav language as value and key as name (Names are unique )

d = {}

name = input("Enter friend name:")
language = input("Enter language name:")
d.update({name:language})
name = input("Enter friend name:")
language = input("Enter language name:")
d.update({name:language})
name = input("Enter friend name:")
language = input("Enter language name:")
d.update({name:language})
name = input("Enter friend name:")
language = input("Enter language name:")
d.update({name:language})

print(d)


