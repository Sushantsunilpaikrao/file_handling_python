import os

file_path = 'task1.txt'

if os.path.exists(file_path):
    os.remove(file_path)
    print(f"The file {file_path} has been deleted.")
else:
    print(f"The file {file_path} does not exist.")
