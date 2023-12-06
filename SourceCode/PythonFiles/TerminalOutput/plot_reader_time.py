def user_reader_time(data):
    # Dictionary to store total reading time per user
    reading_times = {}

    # Iterate over each record
    for record in data:
        user_id = record['visitor_uuid']
        time_spent = record.get('event_readtime', 0)  # Replace 'time_spent' with your actual field name

        # Add the time spent to the user's total
        if user_id in reading_times:
            reading_times[user_id] += time_spent
        else:
            reading_times[user_id] = time_spent

    # Sort users by total reading time, descending
    top_readers = sorted(reading_times.items(), key=lambda x: x[1], reverse=True)
    return top_readers
