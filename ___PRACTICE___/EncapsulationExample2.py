#protected Encapsulation Method using Attributes and methods
class Animal:
    _a ="Dog"#use underscore for Protected 
    def _show(self):
        print("This is the Protected in Encapsulation")
class Human(Animal):
    def show(self):
        print(super()._a)
obj=Human()
obj.show()
obj._show