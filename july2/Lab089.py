f = open('input.png', 'rb')    # stores in numbers
for i in f:
    print(i)              # gives op in binary data

# instead of reading , write it

f = open('input.png', 'rb')    # stores in numbers
f1 = open('output.png', 'wb')
for i in f:
    f1.write(i)

