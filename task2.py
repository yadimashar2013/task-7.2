
file_name = 'my soul.txt'
with open(file_name, mode='r', encoding='utf8') as file:
    for line in file:
        print(line)
print(file.closed) # в конце появляется True, что означает что файл закрыт.