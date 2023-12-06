
def get_unique_visitors_count(data):
    unique_visitors = set()
    for record in data:
        if 'visitor_uuid' in record:
            unique_visitors.add(record['visitor_uuid'])
    return len(unique_visitors)

def get_unique_documents_count(data):
    unique_documents = set()
    for record in data:
        if 'env_doc_id' in record:
            unique_documents.add(record['env_doc_id'])
    return len(unique_documents)

def average_reading_time_per_document(data):
    total_time = {}
    counts = {}

    for record in data:
        if 'event_readtime' in record and 'env_doc_id' in record:
            doc_id = record['env_doc_id']
            read_time = record['event_readtime']

            total_time[doc_id] = total_time.get(doc_id, 0) + read_time
            counts[doc_id] = counts.get(doc_id, 0) + 1

    average_time = {doc: total_time[doc] / counts[doc] for doc in total_time}
    # Convert miliseconds to minutes
    try :
        return round(round(sum(average_time.values()) / len(average_time), 2) / 60000, 2)
    except:
        return 0

def total_visits_count(data):
    total_visits = 0
    for record in data:
        if 'visitor_uuid' in record:
            total_visits += 1
    return total_visits