#membership operators

# in , in not
list1 = [1, 2, 3, 4, 5]

print(4 in list1)
print(4 not in list1)
print(8 in list1)
print(8 not in list1)

# identity operators - checks the identity (compare the memory location of two variables
# is , is not
a = 10
b = 10
c = 20

print(id(a))
print(id(b))
print(id(20))

print(a is b)

print(a is c)
