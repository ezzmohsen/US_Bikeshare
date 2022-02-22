import time
import datetime
import pandas as pd
import numpy as np
"""
You need to place these Datasets at the same path of your project and open it in the same workspace in order to CITY_DATA can store this data sets without errors 
"""

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city,month,day="","",""
    while city not in CITY_DATA:
        city=input("enter the city name (chicago,new york city or washignton) \n").lower()
    # get user input for month (all, january, february, ... , june)
    while month not in ['all','january','february','march','april','may','june']:
        month=input("enter the city name ['all','january','february','march','april','may','june'] \n").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while day not in ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
        day=input("enter the city name ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday'] \n").lower()


    print('-'*40)
    return city, month, day


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("the most common month is: {} \n".format(df['month'].mode()[0]))

    # display the most common day of week
    print("the most common month is: {} \n".format(df['day_of_week'].mode()[0]))

    # display the most common start hour
    print("the most common month is: {} \n".format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("the most common start station is: {} \n".format(df['Start Station'].mode()[0]))
    # display most commonly used end station
    print("the most common end station is: {} \n".format(df['End Station'].mode()[0]))
    # display most frequent combination of start station and end station trip
    df['combined_station']=df['Start Station']+df['End Station']
    print("the most common combinaed station is: {} \n".format(df['combined_station'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time=df['Trip Duration'].sum()
    seconds=total_time/3600
    print("time traveled is: {}\n".format(str(datetime.timedelta(seconds=seconds))))

    # display mean travel time
    average_duration = round(df['Trip Duration'].mean())/60
    print("average time is: {}\n".format(str(datetime.timedelta(seconds=average_duration))))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("counts of user types are: {}\n".format(df['User Type'].value_counts()))
    # Display counts of gender
    try:
        print("counts of genders are: {}\n".format(df['Gender'].value_counts()))
    except:
        print("no genders found\n")
    # Display earliest, most recent, and most common year of birth
    try:
        print("earlist birth year is: {}\n".format(df['Birth Year'].min()))
        print("recent birth year is: {}\n".format(df['Birth Year'].max()))
        print("most common birth year is: {}\n".format(df['Birth Year'].mode()[0]))
    except:
        print("no birth year found \n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
