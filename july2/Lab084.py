with open('demo.txt', 'r') as file:
    data = file.readlines()
    # print(data)
    for line in data:
        print(line.split(','))


# readline used to read line by line
# readlines  used to read all lines and stores in a list


# read words from file and print in reverse order
with open('demo.txt', 'r') as file:
    data = file.read().split()
    # print(data)
    for word in data[::-1]:
        print(word)