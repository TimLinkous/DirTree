import os

def list_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            print (file)

list_files('test')

# def list2_files(directory, with_path = False):