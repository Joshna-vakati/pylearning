# filter
#########################################################################################
# filter(function, iterable)
# filter() method filters the given sequence with the help of
# a function that tests each element in the sequence to be true or not.
# The function to be used as a filter should return a boolean value.
# filter() method returns an iterator value so we have to typecast it to the list.

def is_even(a):
    return a%2 == 0
lst = [1,2,3,4,5,6,7,8,9,10]
result = filter(is_even, lst)
res = filter(lambda x:x%2==0, lst)
print(list(res))


#zip

# zip returns an iterator of tuples based on the iterable objects.
last1 = [1,2,3,4,5]
last2 = [6,7,8,9,10]
res =[]
for item1, item2 in zip(last1, last2):
    res.append(item1+item2)
print(res)
]
