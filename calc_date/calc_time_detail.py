
import datetime


def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def calc_month_days(year, month):
    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    else:
        if month > 8:
            return 31 - (month % 2)
        else:
            return 30 + (month % 2)


def calc_date():
    birth_year = int(input('Enter your birth year: '))
    birth_month = int(input('Enter your birth month: '))
    birth_day = int(input('Enter your birth day: '))

    birth = datetime.date(birth_year, birth_month, birth_day)
    today = datetime.date.today()

    days_lived = 0

    # the birth's date to the end of birth's year
    for month in range(birth.month, 13):
        if month == birth_month:
            days_lived += calc_month_days(birth.year, birth.month) - birth.day
        else:
            days_lived += calc_month_days(birth.year, birth.month)

    # the birth's year + 1 to the today's year - 1
    for year in range(birth_year + 1, today.year):
        if is_leap_year(year):
            days_lived += 366
        else:
            days_lived += 365

    # 2019/01/01 to the today's day
    for month in range(1, today.month + 1):
        if month == today.month:
            days_lived += today.day
        else:
            days_lived += calc_month_days(today.year, today.month)

    print(days_lived)


calc_date()
