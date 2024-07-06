file = open('demo.txt','r')

content = file.read(10)
print(content)

position = file.tell()   Check the current position of the file pointer
print(position)

file.close()