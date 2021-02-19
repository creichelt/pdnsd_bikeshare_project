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


# display the most common month
print("Most common month:", df['month'].mode()[0])
# display the most common day of week
print("Most common day:", df['weekday'].mode()[0])
# display the most common start hour
print("Most common start hour:", df['hour'].mode()[0])

# display most commonly used start station
print("The most common Start Station is:", df['Start Station'].value_counts().idxmax())
# display most commonly used end station
print("The most common End Station is:", df['End Station'].value_counts().idxmax())
# display most frequent combination of start station and end station trip
print("The most common trip is:", df.groupby(['Start Station', 'End Station']).size().idxmax())

# display total travel time
print("Total travel time:", df['Trip Duration'].sum())
# display mean travel time
print("Mean travel time:", df['Trip Duration'].mean())

# display counts of user types
print("User types:")
print(df['User Type'].value_counts().to_string())
# display counts of gender
try:
    print("Gender types:")
    print(df['Gender'].fillna('no info').value_counts().to_string())
except:
    print("There is no gender info for", city.capitalize())

# display earliest, most recent, and most common year of birth
try:
    print("The most recent Birth Year is:", int(df3['Birth Year'].max()))
    print("The most earliest Birth Year is:", int(df3['Birth Year'].min()))
    print("The most common Birth Year is:", int(df3['Birth Year'].mode()))
except:
    print("There is no Birth Year info for", city.capitalize())




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
