# 1. Explain the difference between the = operator and the == operator in Python.

# =  used for assigning a value to the variable

# == used for comparing two values wether they are equal or not

a = 2
b = 2

print(a)
print(a == b)


#2. What does the ** operator do in Python, and how is it used?

# ** operator used for exponential

print(2 ** 3)
print(4**4)

#3. What does the ^ operator do in Python, and in what context is it commonly used?

# ^ represents Bitwise XOR in python used for XOR operation on two operands
# it returns true if and only if exactly one of the operands is true.


# xor truth table
# A   B   A^B
# 0	  0	    0
# 0	  1	    1
# 1	  0	    1
# 1	  1	    0

# If both inputs are same inputs, the output is “0”.

print(5^4)

# 5 ->    0101
# 4 ->    0100
# 5^4 ->  0001  = 1
