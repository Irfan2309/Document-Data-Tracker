from graphviz import Digraph
import tkinter as tk
from PIL import Image, ImageTk

# Get the list of all the readers who visited the document
def get_readers_by_document(data, doc_uuid):

    # Initialize the list to store the readers
    all_readers = []

    for record in data:
        # Check if the subject_doc_id is present in the record 
        # if the subject_doc_id is equal to the doc_uuid
        # and if the visitor_uuid is present in the record
        if 'subject_doc_id' in record and  record['subject_doc_id'] == doc_uuid and 'visitor_uuid' in record:
            all_readers.append(record['visitor_uuid'])
    
    # Return the list of readers
    return all_readers

# Get the list of all the documents read by the visitor
def get_document_by_readers(data, visitor_uuid):

    # Initialize the list to store the documents
    all_docs = []

    for record in data:
        # Check if the visitor_uuid is present in the record
        # if the subject_doc_id is present in the record
        # and if the visitor_uuid is equal to the visitor_uuid
        if 'visitor_uuid' in record and record['visitor_uuid'] == visitor_uuid and 'subject_doc_id' in record:
            all_docs.append(record['subject_doc_id'])
    return all_docs

# Get the top 10 documents that are read by the readers who also read the document
def also_likes(data, doc_uuid, visitor_uuid = None, sorting_function=None):

    # If the sorting function is not provided, then use the default sorting function
    if sorting_function is None:
        sorting_function = lambda x: x[1]['count']

    # Get the list of all unique readers who visited the document
    all_readers = set(get_readers_by_document(data, doc_uuid))

    # If the visitor_uuid is provided, then remove the visitor_uuid to the list of readers
    if visitor_uuid is not None:
        all_readers.remove(visitor_uuid)

    # Initialize the dictionary to store the documents
    # The dictionary will have the document id as the key and the value will be a dictionary
    # The value dictionary will have two keys: count and readers 
    # count will store the number of readers who read the document 
    # readers will store the list of all the readers who read the document
    liked_documents = {}
    for reader in all_readers:
            # Get the list of all the documents read by the reader
            documents = set(get_document_by_readers(data, reader))
            for doc in documents:
                # Check if the document is already present in the dictionary
                if doc not in liked_documents:
                    # If the document is not present in the dictionary, then add the document to the dictionary
                    liked_documents[doc] = {'count': 0, 'readers': set()}
                # Increment the count of the document by 1
                liked_documents[doc]['count'] += 1
                # Add the reader to the list of readers who read the document
                liked_documents[doc]['readers'].add(reader)

    # Sort the documents based on the sorting function
    sorted_docs = sorted(liked_documents.items(), key=sorting_function, reverse=True)

    # Return the top 10 documents
    return sorted_docs[:10]

def generate_graph(data, doc_uuid, visitor_uuid = None, sorting_function=None):
    # Create a Digraph object
    dot = Digraph(comment='Also Likes Graph')

    # Highlight the input document and visitor
    mainDocId = doc_uuid[-4:]
    dot.node(mainDocId, mainDocId, style='filled', fillcolor='green')
    
    if visitor_uuid:
        mainVisitorId = visitor_uuid[-4:]
        dot.attr('node', shape='box')
        dot.node(mainVisitorId, mainVisitorId, style='filled', fillcolor='green')
        dot.attr('node', shape='ellipse')
        dot.edge(mainVisitorId, mainDocId)

    # Get the list of "also likes" documents using the also_likes function
    if sorting_function is None:
        sorting_function = lambda x: x[1]['count']
    also_likes_docs = also_likes(data, doc_uuid, visitor_uuid, sorting_function)
    
    # For each "also likes" document, get the readers and create edges
    for doc, info in also_likes_docs:
        docId = doc[-4:]
        # Add the document node
        dot.node(docId, docId)
        readers = info['readers']
        for reader in readers:
            readerId = reader[-4:]
            # Add the reader node
            dot.attr('node', shape='box')
            dot.node(readerId, readerId)
            dot.attr('node', shape='ellipse')
            # Add an edge from reader to the document
            dot.edge(readerId, docId)
    # Generate and save the graph
    print(dot.source) 
    dot.render('also_likes_graph', format='png', cleanup=True)
    # Return the graph
    return dot
    

