# constructor

# used to initialize the object's state
# ●	a constructor is a special method that is automatically called when an object is created from a class.
# ●	It is used to initialize the object's attributes or perform any necessary setup tasks.
# ●	The constructor method in Python is called __init__().

class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        print(f"x = {self.x}, y = {self.y}")

obj1 = MyClass(10, 20)
obj1.display()
obj2 = MyClass(30, 20)
obj2.display()
