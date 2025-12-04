#There are class attributes and instance attributes 
class Car:
    wheels=4
    def __init__(self,name):
        self.name=name
        
    def show(self):
        print(f"Welcome in {self.name}")
        
obj=Car("creta")
obj.show()