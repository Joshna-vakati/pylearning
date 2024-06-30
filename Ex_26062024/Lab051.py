#class attributes

# declared inside the class
# shared and accessed by all class elements and outside the class.
# they are called by class names
# memory of class attributes shared by all the instamces of a class.

class employee:
    #class attributes
    empname = 'joshna'         #empname and empage are class attributes
    empage = 4

    def display(self):
             #if u want to cahnge the values of class atribute for each object u can assign
        print(employee.empname)
        print(employee.empage)
    def show(self):
        print(employee.empname)
        print(employee.empage)

emp1 = employee()

emp1.display()
emp1.show()

print(employee.empname)    # outsude the class also accessible




