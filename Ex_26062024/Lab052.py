# instance attributes

class employee:
    def display(self):
        #instance attributes
        # should declare inside the methods
        self.name = 'joshna'
        self.age = 30
        print(self.name, self.age)
    def show(self):
        self.address = 'Hyd'
        print(self.address)

obj1 = employee()
obj1.display()
obj1.show()

print(obj1.name, obj1.age, obj1.address)