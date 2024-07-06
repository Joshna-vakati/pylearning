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
