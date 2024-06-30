# global attributes

# poweful-sharing
# count
# caching
# frequently
# global keyword
# scope  -   access function , access class , acess module


# accessed by all instances of a class.

Dep = 'Training' # global variable
class Employee:
    def getinfo(self):
        self.empname = 'joshna'
        self.empid = 14
        print(self.empname, self.empid)
        print(Dep)
    def display(self):
        print(self.empname, self.empid)

obj = Employee()
obj.getinfo()
obj.display()