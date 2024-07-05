# abstraction
# hiding the irrelevant data and displaying only relevant data

#we can achieve data abstraction by using abstract classes
# and abstract classes can be created using abc (abstract base class) module
# and abstractmethod of abc module


from abc import ABC, abstractmethod


class Father(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def loan(self):
        pass


class Pramod(Father):
    def loan(self):
        print("Loan given")


pramod = Pramod("rancho")
pramod.loan()