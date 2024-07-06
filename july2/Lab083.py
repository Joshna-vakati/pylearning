file = open('demo.txt', 'r')
print(file.read())    # read the entire file
file.close()

print('reading characters\n')


file = open('demo.txt', 'r')
print(file.read(3))    # read the first 3 characters
file.close()

print('reading 1st line in the text file\n')

file = open('demo.txt', 'r')
print(file.readline())     # read the first line
print(file.readline())     # reads second line
file.close()

print('reading each line\n')

file = open('demo.txt', 'r')
for line in file:
    print(line)    # reads and prints each line

print('reading file using with\n'')
    # no need to close the file with close() mmethod

with open('demo.txt', 'r') as file:   # 'r' is default mode
    print(file.read())
