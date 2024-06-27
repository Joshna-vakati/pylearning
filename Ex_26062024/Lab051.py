class employee:
    #class attributes
    empname = 'joshna'         #empname and empage are class attributes
    empage = 4

    def display(self):
        self.empname = 'vijay'         #if u want to cahnge the values of class atribute for each object u can assign
        print(self.empname)
        print(self.empage)
    def show(self):
        self.empname = 'babu'
        print(self.empname)
        print(self.empage)

emp1 = employee()

emp1.display()
emp1.show()


