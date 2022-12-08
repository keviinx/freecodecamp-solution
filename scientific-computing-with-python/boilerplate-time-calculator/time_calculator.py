def add_time(start, duration, day = None):

    # variable initialize
    new_time_hour = 0
    new_time_am_pm = None
    new_time_days = 0
    days_of_the_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    # Check whether AM or PM
    if start.split()[1] == "PM":
        # take the front of time
        start_hour = int(start.split(":")[0]) + 12

    # Handle for AM
    else:
        # Just get the hour directly
        start_hour = start.split(":")[0]

    # Get the start minute
    start_minute = (start.split(":")[1]).split()[0]

    # Get the duration hour
    duration_hour = duration.split(":")[0]

    # Get the duration minute
    duration_minute = duration.split(":")[1]

    # Add the minutes
    new_time_minute = int(start_minute) + int(duration_minute)

    # Check if the minutes is more than 60
    if (new_time_minute > 60):
        new_time_hour += 1
        new_time_minute -= 60

    # Total the hour
    new_time_hour += int(start_hour) + int(duration_hour)

    # Check if more than 24 hours
    if (new_time_hour > 24):
        new_time_days = int(new_time_hour / 24)
        new_time_hour = new_time_hour % 24

    # Check if PM or AM
    if (new_time_hour == 12):
        new_time_am_pm = "PM"
    elif (new_time_hour > 12 and new_time_hour < 24):
        new_time_am_pm = "PM"
        new_time_hour -= 12
    elif (new_time_hour == 24 or new_time_hour == 0):
        new_time_hour = 12
        new_time_am_pm = "AM"
    else:
        new_time_am_pm = "AM"

    # check if minutes is lower than 10
    if (new_time_minute < 10):
        new_time_minute = "0" + str(new_time_minute)

    # append the text to output
    # No day argument
    if day == None:
        if (new_time_days == 1):
            new_time = str(new_time_hour) + ":" + str(new_time_minute) + " " + str(new_time_am_pm) + " (next day)"
        elif (new_time_days > 1):
            new_time = str(new_time_hour) + ":" + str(new_time_minute) + " " + str(new_time_am_pm) + " (" + str(new_time_days) + " days later)"
        else:
            new_time = str(new_time_hour) + ":" + str(new_time_minute) + " " + str(new_time_am_pm)
    # have day argument
    else:

        # get the index of the new day
        new_time_day_of_the_week_index = (days_of_the_week.index(day.lower()) + new_time_days) % 7
        new_time_day_of_the_week = days_of_the_week[new_time_day_of_the_week_index].capitalize()

        if (new_time_days == 1):
            new_time = str(new_time_hour) + ":" + str(new_time_minute) + " " + str(new_time_am_pm) + ", " + new_time_day_of_the_week + " (next day)"
        elif (new_time_days > 1):
            new_time = str(new_time_hour) + ":" + str(new_time_minute) + " " + str(new_time_am_pm) + ", " + new_time_day_of_the_week + " (" + str(new_time_days) + " days later)"
        else:
            new_time = str(new_time_hour) + ":" + str(new_time_minute) + " " + str(new_time_am_pm) + ", " + new_time_day_of_the_week

    return new_time