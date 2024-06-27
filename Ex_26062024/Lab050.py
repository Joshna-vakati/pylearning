class person:
    #attributes

    # methods

    def talk(self):
        print('I can talk')

    def walk(self):
        print('i can walk')

obj1 = person()
# person.walk(obj1)   # calling method with the help of class (static method )
obj1.walk()            # calling method with the help of object (non static method)
obj1.talk()

