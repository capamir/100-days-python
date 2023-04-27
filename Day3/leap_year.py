def is_leap(year):
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        else:
            if year % 400 == 0:
                return True
            return False
    else:
        return False

year = int(input('give me a year: '))

if is_leap(year):
    print('leap year')
else:
    print('not leap year')