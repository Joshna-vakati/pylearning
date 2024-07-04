import multipledispatch as md


# over loading
class A:

    def add(self, a ):
        self.a = a
        return self.a

    def add(self, a, b ):
        self.a = a
        self.b = b
        return self.a + self.b


obj = A()
print(obj.add(3, 4))
 # it should go to add(self, a) method
# but python takes only latest method , so python does not support overloading.
# print(obj.add(3))


print('Alternative solutions')
print('default argumrnts')
#but we can achive by some tricks

# 1. default arguments

class Student:
    def sub(self, a ):
        self.a = a
        return self.a
    def sub(self, a, b=0):
        self.a = a
        self.b = b
        return self.a - self.b

obj1 = Student()
print(obj1.sub(3))
# print(obj1(3))

print('Multiple dispatch operator')

# 2) using multiple dispatch decorator
class new:
    @md.dispatch(int, int)
    def display(a, b):
        return a , b

    @md.dispatch(int)
    def display(a):
        return a

    @md.dispatch(float,float,float)
    def display(a, b, c):
        return a , b , c

print(display(2))
print(display(2,4))
print(display(2.0, 4.0, 6.0))