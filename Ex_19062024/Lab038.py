#  map
# map() function returns a map object of the results after
# applying the given function to each item of a given iterable

#syntax

# map(fun, *iter)
# map(lambda arg: expression, iterable1, iterable2,...)

# Example 1: Passing a lambda function to the map() function

# Define a lambda function to multiply a number by 2
double = lambda x: x * 2

lst1 = [1, 2, 3, 4, 5]
# Use map() with the lambda function to double each element in lst1
print(list(map(double, lst1)))


#adding 2 lists  using map
l1 =[1,2,3,4,5]
l2 =[6,7,8,9,10]

res = map(lambda x, y:x+y , l1, l2)
print(list(res))

#without map

for item1, item2 in zip(l1, l2):
    # print(item1)
    # print(item2)
    print(item1+item2)


