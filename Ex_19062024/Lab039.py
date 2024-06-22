# enumerator
#
# The enumerate () method adds a counter to an iterable and
# returns it in the form of an enumerating object.
# This enumerated object can then be used directly
# for loops or converted into a list of tuples using the list() function.
#
# Syntax: enumerate(iterable, start=0)
#
# Return: Returns an iterator
# with index and element pairs from the original iterable
#
# and returns an enumerate object that iterates over the pairs.

# Examples:
#
# Input: list1 = [3, 4, 5, 6, 7]
# Output: [(0, 3), (1, 4), (2, 5), (3, 6), (4, 7)]

lst =  [11,22,33,44,55]
for index, item in enumerate(lst):
    print(index, item)
