# Inheritance
# Acquire the Attributes and Behaviour
# Data members and Methods

# 3BHK Hourse -F -> Inheritance - Son -
# concept in object-oriented programming (OOP)
# that allows a class (child class) to inherit attributes and methods
# from another class (parent class)

# Types of Inheritance

# Single - 80%  - # API, Web Automation - 80% -> Single
# Multiple
# Multi level
# Hybrid
# Hierarchical


# single
# base class
class A:
    def func1(self):
        print('this is base class ')

# derived class
class B(A):
    def func2(self):
        print('this is derived class')

# creating a obj for derived class

obj = B()
obj.func1()        # parent method
obj.func2()        # child method


# creating a obj for base class

obj1 = A()
obj1.func1()       # parent method  (cannot access the child method)
