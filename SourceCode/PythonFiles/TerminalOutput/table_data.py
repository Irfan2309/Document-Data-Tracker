from collections import defaultdict

# Function to proces the reading data and return the result
def process_reading_data(data):
    # Create a dictionary to store the total read time and the number of documents read by each user
    total_read_time = defaultdict(int)
    # Create a dictionary to store the number of documents read by each user
    doc_count = defaultdict(int)
    # For every record in the data
    for record in data:
        # Get the user id
        user_id = record['visitor_uuid']
        # Increment the number of documents read by the user
        doc_count[user_id] += 1
        # If the record has the read time
        if 'event_readtime' in record:
            # Add the read time to the total read time of the user
            total_read_time[user_id] += record['event_readtime']
    
    # Create a list to store the result
    result = []
    # For every user id in the doc_count dictionary
    for user_id in doc_count:
        # Calculate the average read time of the user
        avg_read_time = round((total_read_time[user_id] / doc_count[user_id]),2) if doc_count[user_id] > 0 else 0
        # Append the user id, number of documents read by the user and the average read time of the user to the result list
        result.append((user_id, doc_count[user_id], avg_read_time))
    # Sorting the result list based on the number of documents read by the user
    result.sort(key=lambda x: x[1], reverse=True)
    # Return the result list
    return result

# Function to process the document data and return the result
def process_document_data(data):
    # Create a dictionary to store the total read time and the number of users who read the document
    total_read_time = defaultdict(int)
    # Create a dictionary to store the number of users who read the document
    user_count = defaultdict(set)

    # For every record in the data
    for record in data:
        # Get the user id
        user_id = record['visitor_uuid']
        # Get the document id
        if 'subject_doc_id' in record:
            doc_id = record['subject_doc_id']
        
        # Adding the user id to the set of users who read the document
        user_count[doc_id].add(user_id)

        # If the record has the read time
        if 'event_readtime' in record:
            # Add the read time to the total read time of the document
            total_read_time[doc_id] += record['event_readtime']

    # Create a list to store the result 
    result = []

    # For every document id in the user_count dictionary
    for doc_id in user_count:
        # Calculate the average read time of the document
        avg_read_time = round((total_read_time[doc_id] / len(user_count[doc_id])),2) if user_count[doc_id] else 0
        # Append the document id, number of users who read the document and the average read time of the document to the result list
        result.append((doc_id[-4:], len(user_count[doc_id]), avg_read_time))

    # Sorting the result list based on the number of users who read the document
    result.sort(key=lambda x: x[1], reverse=True)

    # Return the result list
    return result

    