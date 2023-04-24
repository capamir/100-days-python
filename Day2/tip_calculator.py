print('wellcome to tip calculator')
total_bill = float(input('what was the total bill? $'))
people = int(input('How many people to splite the bill? '))
tip_percentage = int(input('what percentage of the bill would you like to give? 10, 12 or 15? '))

final_bill = total_bill * (1 + tip_percentage / 100)
each_person = round(final_bill / people, 2)
print(f'each person should pay: ${each_person}')
