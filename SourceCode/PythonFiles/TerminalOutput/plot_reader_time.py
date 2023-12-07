# Function to plot the total reading time per user
def user_reader_time(data):

    # Dictionary to store total reading time per user
    reading_times = {}

    # For loop for each record in the data
    for record in data:
        # Get the user ID and time spent
        user_id = record['visitor_uuid']

        # Getting the time spent on the page
        time_spent = record.get('event_readtime', 0)

        # Add the time spent to the user's total
        if user_id in reading_times:
            reading_times[user_id] += time_spent
        else:
            reading_times[user_id] = time_spent

    # Covert time to seconds
    for user_id in reading_times:
        reading_times[user_id] = round(reading_times[user_id] / 1000)

    # Sort users by total reading time, descending
    top_readers = sorted(reading_times.items(), key=lambda x: x[1], reverse=True)

    # Return the top readers
    return top_readers
