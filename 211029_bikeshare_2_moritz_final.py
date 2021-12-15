import time
import pandas as pd
import numpy as np

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
    # Get user input for city (chicago, new york city, washington)
    while True:
        print('\n')
        city = input('Please tell me the city you would like to receive bikeshare statistics on (Chicago, New York City, Washington): ').lower()
        if city in ['chicago','new york city','washington']:
            break
        else:
            print('\n')
            print('Unfortunately this is not a valid input. Please give me one of the cities shown in parenthesis.')

    # Get user input for month (all, january, february, ... , june)
    while True:
        print('\n')
        month = input('Now, please tell me the month you would like to receive bikeshare statistics from (all, January, February, ... , June): ').lower()
        if month in ['all','january','february','march','april','may','june']:
            break
        else:
            print('\n')
            print('Unfortunately this is not a valid input. Please give me one of the possible month input shown in parenthesis.')

    # Get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        print('\n')
        day = input('Please tell me now the day of week you would like to receive bikeshare statistics from (all, Monday, Tuesday, ... Sunday): ').lower()
        if day == 'all':
            break
        elif day == 'monday':
            break
        elif day == 'tuesday':
            break
        elif day == 'wednesday':
            break
        elif day == 'thursday':
            break
        elif day == 'friday':
            break
        elif day == 'saturday':
            break
        elif day == 'sunday':
            break
        else:
            print('\n')
            print('Unfortunately this is not a valid input. Please give me one of the possible day of week input shown in parenthesis.')


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
    # Load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create the new columns 'month' and 'day_of_week'
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # Filter by month if applicable
    if month != 'all':
        # Use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # Filter by month to create the new dataframe
        df = df[df["month"] == month]

    # Filter by day of week if applicable
    if day != 'all':
        # Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month and the corresponding count
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    popular_month = df['month'].mode()[0]
    popular_month_count = (df['month'] == popular_month).sum()

    # Use the popular_month int as an index to get the coresponding month name from the months list
    print('The most common month is: {} (Count: {})\n'.format(months[popular_month - 1], popular_month_count))


    # Display the most common day of week and the corresponding count
    popular_dow = df['day_of_week'].mode()[0]
    popular_dow_count = (df['day_of_week'] == popular_dow).sum()
    print('The most common day of week is: {} (Count: {})\n'.format(popular_dow, popular_dow_count))

    # Display the most common start hour and the corresponding count
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    popular_hour_count = (df['hour'] == popular_hour).sum()
    print('The most common hour is: {} (Count: {})\n'.format(popular_hour, popular_hour_count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station and the corresponding count
    popular_start_station = df['Start Station'].mode()[0]
    popular_start_station_count = (df['Start Station'] == popular_start_station).sum()
    print('The most commonly used start station is: {} (Count: {})\n'.format(popular_start_station, popular_start_station_count))

    # Display most commonly used end station and the corresponding count
    popular_end_station = df['End Station'].mode()[0]
    popular_end_station_count = (df['End Station'] == popular_end_station).sum()
    print('The most commonly used end station is: {} (Count: {})\n'.format(popular_end_station, popular_end_station_count))

    # Display most frequent combination of start station and end station trip and the corresponding count
    # First creat the new column 'start_end_combination' as a basis to count the most popular start-end-route
    df['start_end_combination'] = df['Start Station'] + ' ---> ' + df['End Station']
    popular_start_end_combination = df['start_end_combination'].mode()[0]
    popular_start_end_combination_count = (df['start_end_combination'] == popular_start_end_combination).sum()
    print('The most frequent combination of start station and end station trip: {} (Count: {})\n'.format(popular_start_end_combination, popular_start_end_combination_count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is: {} seconds.\n'.format(total_travel_time))

    # Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The average trip duration is: {} seconds.\n'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print('These are the counts of user types:\n')
    print(user_types_count)
    print('\n')

    # Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('These are the counts of genders:\n')
        print(gender_count)
        print('\n')
    except KeyError:
        # Handle KeyError if Washington is chosen as there is no gender information
        print('There is no gender information in the data set.\n')

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_yob = df['Birth Year'].min()
        most_recent_yob = df['Birth Year'].max()
        most_common_yob = df['Birth Year'].mode()[0]
        most_common_yob_count = (df['Birth Year'] == most_common_yob).sum()

        print('The earliest year of birth is: {}\n'.format(int(earliest_yob)))
        print('The most recent year of birth is: {}\n'.format(int(most_recent_yob)))
        print('The most common year of birth is: {} (Count: {})\n'.format(int(most_common_yob), most_common_yob_count))

    except KeyError:
        # Handle KeyError if Washington is chosen as there is no birth year information
        print('There is no birth year information in the data set.\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_raw_data(df):
    """Displays raw data of the dataframe to the user."""

    # Prompt the user if they want to see 5 lines of raw data
    view_data = input('\nWould you like to view 5 rows of individual trip data? Please enter yes or no. \n')
    start_loc = 0

    # Display that data if the answer is 'yes' and continue iterating prompts and displaying the next 5 lines of raw data at each iteration
    # Stop the loop when the user says 'no' or there is no more raw data to display
    while(view_data.lower() == 'yes'):
        if(start_loc >= len(df)):
            break
        print(df.iloc[start_loc:(start_loc + 5)])
        start_loc += 5
        view_data = input('Do you wish to continue?: ')


def main():
    while True:
        city, month, day = get_filters()
        print('Thank you. Your input is:\nCity: {}\nMonth: {}\nDay: {}\n'.format(city.title(), month.title(), day.title()))
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
