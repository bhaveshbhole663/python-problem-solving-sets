# To fill in a letter template given with name and date

Letter = '''Dear <Name>
You are selected!
<Date>'''

print(Letter.replace("<Name>", "Bhavesh").replace("<Date>", "19 June 2026"))

print(Letter.replace("<Name>", input("Enter Your Name: ")).replace("<Date>",input("Enter Date: ")))

