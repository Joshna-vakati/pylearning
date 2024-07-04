# overriding
# same method name and same number of arguments in different classes
# is called overriding
class A:
    def sum(self,a,b):
        self.a = a
        print(self.a)
class B(A):
    def sum(self, a, b):
        self.a = a
        self.b = b
        super().sum(a,b)         # execute parent class sum method also
        return self.a+self.b

obj1 = B()
print(obj1.sum(3,4))      # consider local method first
