with open('task1.txt', 'r') as file:
    contents = file.read()

words = contents.split()

word_count = len(words)

print(f'Total number of words: {word_count}')
