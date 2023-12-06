# Importing the dataset
import argparse
from plot_browser import plot_browser
import matplotlib.pyplot as plt
import json
from plot_reader_time import user_reader_time
# from plot_countries import plot_countries

def handle_task_2a():
    print('Task 2a')

def handle_task_2b():
    print('Task 2b')

def handle_task_3a():
    print('Task 3a')

def handle_task_3b(data):
    print('Task 3b')
    plot_browser(data)

def handle_task_4(data):
    top_readers = user_reader_time(data)
    print("\n\n=======================================")
    print("=            Top 10 Readers           =")
    print("=======================================")
    print("=       User ID       =   Read Time   =")
    print("=======================================")
    for i in range(10):
        print("=  {a:16s}   ={p:9d}      =".format(a=top_readers[i][0], p = top_readers[i][1]) )
    print("=======================================\n\n")


def handle_task_5d():
    print('Task 5d')

def handle_task_6():
    print('Task 6')

def handle_task_7():
    print('Task 7')

def handle_file(file_name):
    new_file_name = None
    if file_name == 'issuu_cw2_train':
        new_file_name = '../../../Dataset/build_dataset.txt'
    elif file_name == 'issuu_cw2_test':
        new_file_name = '../../../Dataset/test_dataset.txt'
    
    if new_file_name is None:
        new_file_name = file_name
    
    try:
        with open(new_file_name) as f:
            data = f.readlines()
        data = [json.loads(x.strip()) for x in data]
        return data
    except Exception as e:
        print('Error: ', e)
        return None
    

def handle_tasks(task_id = None, data = None, user_uuid = None, doc_uuid = None):
    if task_id == '2a':
        handle_task_2a()
    elif task_id == '2b':
        handle_task_2b()
    elif task_id == '3a':
        handle_task_3a()
    elif task_id == '3b':
        handle_task_3b(data)
    elif task_id == '4':
        handle_task_4(data)
    elif task_id == '5d':
        handle_task_5d()
    elif task_id == '6':
        handle_task_6()
    elif task_id == '7':
        handle_task_7()
    else:
        print('Invalid Task ID')

def main():
    # Create a parser object
    parser = argparse.ArgumentParser(description='Process some UUIDs.')

    # Add arguments to the parser
    parser.add_argument('-u', '--user_uuid', required=False, help='User UUID')
    parser.add_argument('-d', '--doc_uuid', required=False, help='Document UUID')
    parser.add_argument('-t', '--task_id', required=True, help='Task ID')
    parser.add_argument('-f', '--file_name', required=True, help='JSON File with input data')

    # Parse the arguments
    args = parser.parse_args()
    # print('User UUID       :', args.user_uuid)
    # print('Document UUID   :', args.doc_uuid)
    # print('Task ID         :', args.task_id)
    # print('File Name       :', args.file_name)

    data = handle_file(args.file_name)
    if data is None:
        print('Error: Could not read file')
        return




    
    # Handle tasks
    handle_tasks(args.task_id, data, args.user_uuid, args.doc_uuid)



if __name__ == '__main__':
    main()