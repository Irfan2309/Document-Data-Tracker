# Function to get top readers with their number of documents read and the average time spent reading
from collections import defaultdict
import json


def process_reading_data(data):
    # Data structures to store the total read time and document count per user
    total_read_time = defaultdict(int)
    doc_count = defaultdict(int)

    for record in data:  # Assuming 'data' is a list of dictionaries
        user_id = record['visitor_uuid']
        if 'env_doc_id' in record:
            doc_id = record['env_doc_id']

        # Update document count
        doc_count[user_id] += 1

        # Update total read time if available
        if 'event_readtime' in record:
            total_read_time[user_id] += record['event_readtime']

    # Calculate average read time and prepare the result
    result = []
    for user_id in doc_count:
        avg_read_time = round((total_read_time[user_id] / doc_count[user_id])/1000,2) if doc_count[user_id] > 0 else 0
        result.append((user_id, doc_count[user_id], avg_read_time))

    # Sort the result based on total docs read in descending order
    result.sort(key=lambda x: x[1], reverse=True)
    return result

def process_document_data(data):
    # Data structures to store the total read time and user count per document
    total_read_time = defaultdict(int)
    user_count = defaultdict(set)

    for record in data:
        user_id = record['visitor_uuid']
        if 'subject_doc_id' in record:
            doc_id = record['subject_doc_id']

        # Update user count for the document
        user_count[doc_id].add(user_id)

        # Update total read time if available
        if 'event_readtime' in record:
            total_read_time[doc_id] += record['event_readtime']

    # Calculate average read time and prepare the result
    result = []
    for doc_id in user_count:
        avg_read_time = round((total_read_time[doc_id] / len(user_count[doc_id]))/1000,2) if user_count[doc_id] else 0
        result.append((doc_id[-4:], len(user_count[doc_id]), avg_read_time))

    # Sort the result based on total users read in descending order
    result.sort(key=lambda x: x[1], reverse=True)

    return result