import time
import pandas as pd
import numpy as np

#csv data is uploaded to github in project
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

        # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ("chicago","new york", "washington")
    while True:
        #input must be case insensitive hence is coverted to lower case in order to accept all variations. e.g.washington, Washington, WaSHINgton, WASHINGTON
        city = input("\nWhich city would you like to see data for - Chicago, New York, Washington?: ").lower()
        if city not in cities:
            print ("\nInvalid input. please select from the given cities")
            continue
        else:
            break

        # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all','january','february','march','april','may','june']
    while True:
        month = input ("\nPlease specify the month you're interested in - from January to June, otherwise type 'All' to see all months: ").lower()
        if month not in months:
            print ("\nInvalid input. Please select from the given months")
            continue
        else:
            break
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    #print ('\n')
    days = ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']
    while True:
        day = input ("\nEnter the name of the week you'd like to see, otherwise type 'All' to see all days: ").lower()
        if day not in days:
            print ("\nInvalid input. Please enter a correct day")
            continue
        else:
            break

    print('-'*40)
    #print (city,month,day)
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
 #load data file into a dataframe
    pd.set_option('display.max_columns',200)
    df = pd.read_csv(CITY_DATA[city])

# convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
# extract month and day of week from Start Time to create new columns
#extract hour from Start Time to create new column
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

# filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
# filter by month to create the new dataframe
        df = df[df['month'] == month]
# filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        #df['day_of_week'] returns values like Friday, Monday, etc. The format is title format hence why title method id called
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print ('\nMost common month:', most_common_month)
    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print ('\nMost common day of week:', most_common_day)
    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print ('\nMost common start hour:', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print ('\nMost commonly used start station:', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print ('\nMost commonly used end station:', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Frequent Trip'] = 'From ' + df['Start Station'] + ' to ' + df['End Station']
    common_trip = df['Frequent Trip'].mode()[0]
    print ('\nMost common trip:', common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print ('\nTotal travel time:', total_travel_time, 'seconds')
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print ('\nMean travel time:', mean_travel_time, 'seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print ('\nUser Type Count: ', user_type_count)

    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print ('\nGender Count: ', gender_count)
    except KeyError:
        print ('\n Gender Count: No Data available')
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = int(df['Birth Year'].min())
        print ('\nEarliest birth year: ', earliest_birth_year)
    except KeyError:
        print ('\n Earliest birth year: No Data available')

    try:
        recent_birth_year = int(df['Birth Year'].max())
        print ('\nMost recent birth year: ', recent_birth_year)
    except KeyError:
        print ('\n Most recent birth year: No Data available')

    try:
        common_birth_year =  int(df['Birth Year'].mode()[0])
        print ('\nMost common birth year: ', common_birth_year)
    except KeyError:
          print ('\nMost common birth year: No Data available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def additional_data(df):
    extra_data = input("\n Would you like to see 5 rows of individual trip data? Please enter Yes or No: ").lower()
    start_loc = 0
    while extra_data !='no':
        print (df.iloc[(start_loc):(start_loc + 5)])
        start_loc += 5
        more_data = input("\n Would you like to see the next 5 rows? Please enter Yes or No: ").lower()
        if more_data != 'yes':
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        additional_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
