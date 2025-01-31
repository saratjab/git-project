import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
    while True:
        try:
            city = input('\nWould you like to see data for Chicago, New York , Washington: ')
            if city.lower() != 'chicago' and city.lower() != 'new york' and city.lower() != 'washington':
                raise Exception('\nOops! That city isn\'t on our list.  Please choose from (chicago, new york, washington)')
            else:
                sure = input('\nYou choose "{}" is that\'s what you want [y/n] '.format(city.title()))
                if sure == 'y':
                    break
                else:
                    raise Exception('\nOops! I miss understand what you wnat')
            break
        except Exception as e:
            print(e)


    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('\nWould you like to filter the data by which month (all, Jan, Feb, Mar, Apr, May, June): ')
            if month.lower() != 'jan' and month.lower() != 'feb' and month.lower() != 'mar' and month.lower() != 'apr' and month.lower() != 'may' and month.lower() != 'june' and month.lower() != 'all':
                raise Exception('\nOops! That month isn\'t available.  Please choose from (all, Jan, Feb, Mar, Apr, May, June)')
            else:
                sure = input('\nYou choose "{}" is that\'s what you want [y/n] '.format(month.title()))
                if sure == 'y':
                    break
                else:
                    raise Exception('\nOops! I miss understand what you wnat')
            break
        except Exception as e:
            print(e)

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('\nWould you like to filter the data by which day (all, Su, Mo, Tu, We, Th, Fr, Sa): ')
            if day.lower() != 'mo' and day.lower() != 'tu' and day.lower() != 'th' and day.lower() != 'we' and day.lower() != 'fr' and day.lower() != 'sa' and day.lower() != 'su' and day.lower() != 'all':
                raise Exception('\nOops! That day isn\'t available.  Please choose from (Su, Mo, Tu, Th, We, Fr, Sa)')
            else:
                sure = input('\nYou choose "{}" is that\'s what you want [y/n] '.format(day.title()))
                if sure == 'y':
                    break
                else:
                    raise Exception('\nOops! I miss understand what you wnat')
            break
        except Exception as e:
            print(e)

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
    df['Month'] = df['Start Time'].dt.month_name()

    month_num = 0
    if month == 'jan':
        month_num = 1
    elif month == 'feb':
        month_num = 2
    elif month == 'mar':
        month_num = 3
    elif month == 'apr':
        month_num = 4
    elif month == 'may':
        month_num = 5
    elif month == 'june':
        month_num = 6

    if month_num != 0:
        df = df[df['Start Time'].dt.month == month_num]


    df['Day'] = df['Start Time'].dt.day_name()

    if day == 'su':
        df = df[df['Day'] == 'Sunday']
    elif day == 'mo':
        df = df[df['Day'] == 'Monday']
    elif day == 'tu':
        df = df[df['Day'] == 'Tuesday']
    elif day == 'we':
        df = df[df['Day'] == 'Wednesday']
    elif day == 'th':
        df = df[df['Day'] == 'Thursday']
    elif day == 'fr':
        df = df[df['Day'] == 'Friday']
    elif day == 'sa':
        df = df[df['Day'] == 'Saturday']

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # display the most common month
    month = df['Start Time'].dt.month.mode()[0]
    m = 0
    if month == 1:
        m = 'January'
    elif month == 2:
        m = 'February'
    elif month == 3:
        m = 'March'
    elif month == 4:
        m = 'April'
    elif month == 5:
        m = 'May'
    elif month == 6:
        m = 'June'
    print(f"The most common month is: {m}")


    # display the most common day of week
    print(f"The most common day is: {df['Day'].mode()[0]}")

    # display the most common start hour
    print(f"The most common start hour is: {df['Start Time'].dt.hour.mode()[0]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print(f'The most commonly used start station: {df['Start Station'].mode()[0]}')

    # display most commonly used end station
    print(f'The most commonly used end station: {df['End Station'].mode()[0]}')


    # display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + ' - ' + df['End Station']
    print(f'most frequent combination of start station and end station trip: {df['Trip'].mode()[0]}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print(f'total travel time: {df['Trip Duration'].sum()}')

    # display mean travel time
    print(f'total mean time: {df['Trip Duration'].mean()}')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(f'Count of user type: {df['User Type'].value_counts()}')

    # Display counts of gender
    if 'Gender' in df:
        print(f'Count of genders: {df['Gender'].value_counts()}'
        )
    else:
        print('No genders')


    # Display earliest, most recent, and most common year of birth  
    if 'Birth Year' in df:
        print(f'Earliest year of birth: {df['Birth Year'].max()}')
        print(f'Most recent year of birth: {df['Birth Year'].min()}')
        print(f'Most common year of birth: {df['Birth Year'].mode()[0]}')
    else:
        print('No Birth year')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city.lower(), month.lower(), day.lower())

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        data = input('\nWould you like to view individual data ?[yes or no].\n')
        cnt = 5
        while data.lower() == 'yes':
            print(df.head(cnt))
            cnt += 5
            data = input('\nWould you like to view individual data ? Enter yes or no.\n')
            if cnt >= len(df):
                print(df.head(cnt))
                print('That\'s all the data')
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
