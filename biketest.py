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

def month_choice():
    while True:
        month = input("Please choose a month (January, February, March, April, May, June, or 'all'):")
        if month.lower() in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            return month.lower()
        else:
            wrong_input()

def day_choice():
    while True:
        day = input("Please choose a day of the week: (Monday, Tuesday, Wednesday, ..., or 'all'):")
        if day.lower() in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
            return day.lower()
        else:
            wrong_input()

def choose():
    choice = input("Would you like to filter by month, day, or not at all (month/day/none)?")
    if choice.lower() == 'month':
        month_choice()
    elif choice.lower() == 'day':
        day_choice()
    elif choice.lower() == 'none':
        month = 'all'
        day = 'all'

# choose()






def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("")
    print("Hello! Let's explore some US bikeshare data!")
    print("")

    # get user input for city (chicago, new york city, washington)
    while True:
        city = input('Please choose a city: Chicago, New York City, or Washington:')
        if city.lower() in ('chicago', 'new york city', 'washington'):
            print('')
            break
        else:
            wrong_input()

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please choose a month (January, February, March, April, May, June, or 'all'):")
        if month.lower()  in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print('')
            break
        else:
            wrong_input()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please choose a day of the week: (Monday, Tuesday, Wednesday, ..., or 'all'):")
        if day.lower()  in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
            print('')
            break
        else:
            wrong_input()

    print("-"*41)
    return city.lower(), month.lower(), day.lower()


######## TO DO

# if not all months/days, filter time stats function

# fix wrong choice break
# fix gender sorting
# fix city reference in gender (WAS only)
