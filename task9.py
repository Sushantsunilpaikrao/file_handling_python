import os

file_path = 'task1.txt'

if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        contents = file.read()
    print(contents)
else:
    print(f"The file {file_path} does not exist.")
