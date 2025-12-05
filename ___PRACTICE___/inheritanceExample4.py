#Single Level Inheritance 

class Animal:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"Your name is {self.name}")
        
class Human(Animal):
    pass

obj1=Human("Prathmesh Patil")
obj=Animal("Lion")
obj1.show()
obj.show()