class calc:

    def __init__(self):
        self.a = 10
        self.b = 20
    def sum(self):
        return self.a +self.b
    def sub(self) -> object: # return type
        print(self.a - self.b)
    def mul(self):
        print(self.a*self.b)

obj1 = calc()
res = obj1.sum()
print(res)

