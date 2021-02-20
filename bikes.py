import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def wrong_input():
    """ outputs info before loop restarts, if user enters incorrect input """
    print("\nThat's not a valid choice.\n")

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

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    # if month != 'all':
    #     # use the index of the months list to get the corresponding int
    #     months = ['january', 'february', 'march', 'april', 'may', 'june']
    #     month = months.index(month) + 1
    #
    #     # filter by month to create the new dataframe
    #     df = df[df['month'] == month]
    #
    # # filter by day of week if applicable
    # if day != 'all':
    #     # filter by day of week to create the new dataframe
    #     df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("Most common month:", df['month'].mode()[0])
    # display the most common day of week
    print("Most common day:", df['weekday'].mode()[0])
    # display the most common start hour
    print("Most common start hour:", df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-"*41)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    # display most commonly used start station
    print("The most common Start Station is:", df['Start Station'].value_counts().idxmax())

    # display most commonly used end station
    print("The most common End Station is:", df['End Station'].value_counts().idxmax())

    # display most frequent combination of start station and end station trip
    print("The most common trip is:", df.groupby(['Start Station', 'End Station']).size().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-"*41)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    # display total travel time
    print("Total travel time:", df['Trip Duration'].sum())

    # display mean travel time
    print("Mean travel time:", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-"*41)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print("\nCalculating User Stats...\n")
    start_time = time.time()

    # display counts of gender
    try:
        print("Gender information:")
        print(df['Gender'].fillna('no info').value_counts().to_string())
        print("")
    except:
        print("There is no gender info")
        print("")

    # removing rows with NaN from DataFrame
    df = df.dropna(axis=0)

    # display earliest, most recent, and most common year of birth
    try:
        print("Age information:")
        print("The most recent Birth Year is:", int(df['Birth Year'].max()))
        print("The most earliest Birth Year is:", int(df['Birth Year'].min()))
        print("The most common Birth Year is:", int(df['Birth Year'].mode()))
    except:
        print("There is no Birth Year info")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-"*41)

def raw_data(df):
    """
    Asks if user wants to see the raw data and returns data in sets of 5,
    asking after every 5 results if they want to see more
    """

    raw = input('Do you want to see the raw data (yes/no)?')
    while True:
        if raw.lower() == 'yes':
            i=0
            print(df.loc[i:i+4])
            for num in range(0,len(df.index)):
                more_data = input('Do you want to see more data (yes/no)?')
                if more_data.lower() == 'yes':
                    i+=5
                    print(df.loc[i:i+4])
                elif more_data.lower() == 'no':
                    break
                else:
                    wrong_input()
            break
        elif raw.lower() == 'no':
            break
        else:
            wrong_input()

def restart():
    """ asks if program should be restarted and triggers restart if required """

    restart = input('\nWould you like to restart? Enter yes or no.\n')
    while True:
        if restart.lower() == 'yes':
            break
        elif restart.lower() == 'no':
            print("bye")
            return
        else:
            wrong_input()
    return


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        # time_stats(df)
        # station_stats(df)
        # trip_duration_stats(df)
        user_stats(df)
        # raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() == 'yes':
            pass
        elif restart.lower() == 'no':
            print("bye")
            break
        else:
            wrong_input()

if __name__ == "__main__":
	main()
