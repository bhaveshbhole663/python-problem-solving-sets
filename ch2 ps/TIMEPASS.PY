# small  mini project 

Freelincer_name = "Bhavesh"
Project_name = "Daily Ledger"
hours_worked = 20
hourly_billing_rate = 12.5
deposite_paid = True

gross_income = hours_worked*hourly_billing_rate
tax_deduction = gross_income*(18/100)
net_income = gross_income-tax_deduction

daily_target = 200.0
hit_target = net_income >daily_target

print("Freelincer:",Freelincer_name)
print("Project :",Project_name)
print("Gross Income :", gross_income)
print("Net Income :",net_income)
print("Did we hit the daily target :",hit_target)
