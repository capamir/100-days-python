age = int(input("what is your current age? "))

years_remining = 90 - age
days_remining = years_remining * 365 + age // 5
weeks_remining = days_remining // 7

print(f'you have {years_remining} years left')
print(f'you have {days_remining} days left')
print(f'you have {weeks_remining} weeks left')
