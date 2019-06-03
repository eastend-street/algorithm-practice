import datetime


birth_year = int(input('Enter your birth year: '))
birth_month = int(input('Enter your birth month: '))
birth_day = int(input('Enter your birth day: '))
birth = datetime.date(birth_year, birth_month, birth_day)
today = datetime.date.today()
print(f'The number of days is {(today - birth).days}')
