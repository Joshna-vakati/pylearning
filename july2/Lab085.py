# write mode

file = open('demo.txt', 'w')
file.write('this is the write command\n')
file.write('It allows us to write in a particular file\n')
file.close()


# read mode

file = open('demo.txt', 'r')
print(file.read())



with open('demo.txt', 'w') as file:
    file.write('this is the write command\n')   #overwrites the existing data

# write()  add single line to the file
# writelines()  adds multiple lines to the file

with open('demo.txt', 'w') as f:
    f.writelines(['yes\n', 'writelines\n', 'used\n' , 'for\n', 'writing multiple lines\n'])
