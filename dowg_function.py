import re
import datetime
import calendar

# this algorithm works from the day 1/3/1100 to the year 4000 not included (idk if it works beyond 3999 cause i can't check it on google)

def dow(date):

# while True:
#     d = input('Enter date(dd/mm/yyyy): ')
#     if d == 'done': break
#     try:
    try:
        date = re.split('-', date)

        day = int(date[0])
        month = int(date[1])
        year = int(date[2])

        dayOfWeek = int()

    # which day is Doomsday
        century = int(str(year)[:2]) - 20
        if century < 0:
            while century < -4:
                century += 4
            if century == -1: dayOfWeek = 3
            if century == -2: dayOfWeek = 5
            if century == -3: dayOfWeek = 0
            if century == -4: dayOfWeek = 2

        if century == 0: dayOfWeek = 2

        if century > 0:
            while century > 4:
                century -= 4
            if century == 1: dayOfWeek = 0
            if century == 2: dayOfWeek = 5
            if century == 3: dayOfWeek = 3
            if century == 4: dayOfWeek = 2

    # now based on the century's Doomsday, we can know which day is the first Doomsday (3rd January or 4th on leap year)
        decade = int(str(year)[2:])
        leapYears = 0
        dayOfWeek += decade
        if decade > 3:
            while decade > 3:
                leapYears += 1
                decade -= 4
        dayOfWeek += leapYears

    # now we just need to add how many days have past since 3rd of January or 4th of January (leap year)
        if calendar.isleap(year):
            d0 = datetime.date(year, 1, 4)
            d1 = datetime.date(year, month, day)
            delta = (d1 - d0).days
        else:
            d0 = datetime.date(year, 1, 3)
            d1 = datetime.date(year, month, day)
            delta = (d1 - d0).days

        dayOfWeek += delta

        if dayOfWeek >= 7:
            while dayOfWeek >= 7:
                dayOfWeek -= 7

        if dayOfWeek < 0:
            if dayOfWeek == -1: dayOfWeek += 7
            if dayOfWeek == -2: dayOfWeek += 7
            if dayOfWeek == -3: dayOfWeek += 7

    # now we need to convert the number into the actual day of the dayOfWeek
    # print(dayOfWeek)
        if dayOfWeek == 0: dayOfWeek = 'Sunday'
        if dayOfWeek == 1: dayOfWeek = 'Monday'
        if dayOfWeek == 2: dayOfWeek = 'Tuesday'
        if dayOfWeek == 3: dayOfWeek = 'Wednesday'
        if dayOfWeek == 4: dayOfWeek = 'Thursday'
        if dayOfWeek == 5: dayOfWeek = 'Friday'
        if dayOfWeek == 6: dayOfWeek = 'Saturday'

        return dayOfWeek

    except:
        return "Invalid input, try again"

# except:
# print('Invalid input, try again')
# continue

# while True:
#     date = input('Enter date(dd/mm/yyyy): ')
#     if date == 'done': break
#     try:
#         d = dow(date)
#     except:
#         print('Invalid input, try again')
#         continue
