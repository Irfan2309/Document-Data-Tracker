# Function to return count of unique visitors
def get_unique_visitors_count(data):
    # Create a set of unique visitors
    unique_visitors = set()
    # FOr every record in data
    for record in data:
        # If visitor_uuid is present in record
        if 'visitor_uuid' in record:
            # Add visitor_uuid to unique_visitors set
            unique_visitors.add(record['visitor_uuid'])
    # Return length of unique_visitors set
    return len(unique_visitors)

# Function to return count of unique documents
def get_unique_documents_count(data):
    # Create a set of unique documents
    unique_documents = set()
    # For every record in data
    for record in data:
        # If env_doc_id is present in record
        if 'env_doc_id' in record:
            # Add env_doc_id to unique_documents set
            unique_documents.add(record['env_doc_id'])
    # Return length of unique_documents set
    return len(unique_documents)

# Function to return count of unique visitors per document
def average_reading_time_per_document(data):
    # Create a dictionary to store total reading time per document
    total_time = {}
    # Create a dictionary to store count of visitors per document
    counts = {}
    # For every record in data
    for record in data:
        # If event_readtime and env_doc_id are present in record
        if 'event_readtime' in record and 'env_doc_id' in record:
            # Store env_doc_id and event_readtime in variables
            doc_id = record['env_doc_id']
            read_time = record['event_readtime']

            # Add read_time to total_time dictionary
            total_time[doc_id] = total_time.get(doc_id, 0) + read_time
            counts[doc_id] = counts.get(doc_id, 0) + 1

    # Calculate average reading time per document
    average_time = {doc: total_time[doc] / counts[doc] for doc in total_time}

    # Convert miliseconds to seconds
    try :
        # Return average reading time per document
        return round(round(sum(average_time.values()) / len(average_time), 2) / 1000, 2)
    except:
        # Return 0 if no data is present
        return 0

# Function to return total visits
def total_visits_count(data):
    # Initialize total_visits to 0
    total_visits = 0
    # For every record in data
    for record in data:
        # If visitor_uuid is present in record
        if 'visitor_uuid' in record:
            # Increment total_visits by 1
            total_visits += 1
    # Return total_visits
    return total_visits