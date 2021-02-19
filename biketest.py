import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
city ='chicago'
df = pd.read_csv(CITY_DATA[city])

# removing columns with NaN
df2 = df.dropna(axis=1)
#removing rows with NaN
df3 = df.dropna(axis=0)


# print('')
print('')
# print(df)

# # convert the Start Time column to datetime
df['Start Time'] = pd.to_datetime(df['Start Time'])
#
# # extract month and day of week from Start Time to create new columns
df['month'] = df['Start Time'].dt.month
df['weekday'] = df['Start Time'].dt.weekday
df['hour'] = df['Start Time'].dt.hour

def wrong_input():
    """ outputs info before loop restarts, if user enters incorrect input """
    print("\nThat's not a valid choice.\n")

def raw_data():
    """
    Asks if user wants to see the raw data and returns data in sets of 5,
    asking after every 5 if they want to see more
    """

    while True:
        raw = input('Do you want to see the raw data (yes/no)?')
        if raw.lower() == 'yes':
            i=0
            for num in range(0,len(df.index)):
                print(df.loc[i:i+4])
#######
                more_data = input('Do you want to see more data (yes/no)?')
                if more_data.lower() == 'yes':
                    i+=5
                elif more_data.lower() == 'no':
                    break
####wrong_ input()
            break
        elif raw.lower() == 'no':
            break
        else:
            wrong_input()

# raw_data()

def restart():
    """ asks if program should be restarted and triggers restart if required """
    while True:
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() in ('yes','no'):
            if restart.lower() == 'yes':
                break
            else:
                False
                print("bye")
        else:
            break

restart()


# restart = input('\nWould you like to restart? Enter yes or no.\n')
# if restart.lower() != 'yes':
#     break



######## TO DO

# filter: by month or day or not at all
# display raw data 5 entries at a time with question to quit


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
