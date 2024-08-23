my_list = ['Item 1', 'Item 2', 'Item 3']

with open('task1.txt', 'w') as file:
    for item in my_list:
        file.write(item + '\n')
