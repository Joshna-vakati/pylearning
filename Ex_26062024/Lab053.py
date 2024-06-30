# local attribute

# declared inside the block
# scope - local scope
# accessed only inside the block
# acessed - attribute name


class Employee:
    def getInfo(self):
        name = 'Rahul'
        age = 23
        address = 'Hyd'

        print(name, age, address)
    def disInfo(self):
        print(name, age, address)

obj =  Employee()
obj.getInfo()
# obj.disInfo()