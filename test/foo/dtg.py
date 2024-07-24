import os
import sys
from pathlib import Path

# def list_files(directory):
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             print (file)

# list_files('test')

def list_files(directory):
    for root, dirs, files, in os.walk(directory):
        print(f'Directory: {root}')
        for file in files:
            print(f'Files: {file}')
        # for name in dirs + files:
        #     if with_paths:
        #         relative_path = os.path.relpath(os.path.join(root, file), directory)
        #         print(relative_path)
        #     else:
        #         print(name)

def list_files_pathlib(directory):
    pth = Path(directory)
    for file_path in pth.rglob('*'):
        if file_path.is_file():
            print(f"File: {file_path}")
        elif file_path.is_dir():
            print(f"Directory: {file_path}")



if __name__ == "__main__":
    directory = 'test'

    list_files(directory)
    list_files_pathlib(directory)