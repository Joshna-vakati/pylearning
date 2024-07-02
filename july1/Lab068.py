# Hierarchical Inheritance

# Father - Multiple Children

class A:
    def func1(self):
        print('this is base class ')

# derived class
class B(A):
    def func2(self):
        print('this is derived 1 class')

class C(A):
    def func3(self):
        print('this is derived 2  class')

class D(A):
    def func4(self):
        print('this is derived 3 class')







# creating a obj for derived one class

obj = B()
obj.func1()        # parent method
obj.func2()        # child method

# creating a obj for derived two class

obj1 = C()
obj1.func1()        # parent method
obj1.func3()        # child method

# creating a obj for derived three class

obj2 = D()
obj2.func1()        # parent method
obj2.func4()        # child method




# creating a obj for base class

obj1 = A()
obj1.func1()       # parent method  (cannot access the child method)

