import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
city ='chicago'
df = pd.read_csv(CITY_DATA[city])

# print('')
print('')

# # convert the Start Time column to datetime
df['Start Time'] = pd.to_datetime(df['Start Time'])
# # extract month and day of week from Start Time to create new columns
df['month'] = df['Start Time'].dt.month
df['weekday'] = df['Start Time'].dt.weekday
df['hour'] = df['Start Time'].dt.hour

def wrong_input():
    """ outputs info before loop restarts, if user enters incorrect input """
    print("\nThat's not a valid choice.\n")






######## TO DO

# filter: by month or day or not at all
# if not all months/days, filter time stats function

# fix gender sorting
# fix city reference in gender (WAS only)


"""
def month_choice:
    while True:
            # get user input for month (all, january, february, ... , june)
            month = input("Please choose a month (January, February, March, April, May, June, or 'all'):")
            if month.lower()  in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
                print('')
                break
            else:
                wrong_input()

def day_choice:
        while True:
            day = input("Please choose a day of the week: (Monday, Tuesday, Wednesday, ..., or 'all'):")
            if day.lower()  in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
                print('')
                break
            else:
                wrong_input()

while True:
    choice = input("Would you like to filter by month, day, or not at all (type 'none')?")
    if choice.lower() = 'month':
        month_choice()
    else if choice.lower() = 'day':
        day_choice()
    else if choice.lower() = 'none':
        break

return city.lower(), month.lower(), day.lower()
"""


# def timestamp(start_time):
#     """ outputs runtime at the end of a function """
#     # start_time = time.time()
#
#     print("\nThis took %s seconds." % (time.time() - start_time))
#     print("-"*41)
