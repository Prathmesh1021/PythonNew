#There Are Class Attributes And Instance Attributes
class car:
    wheels=4#Class Attributes
    def __init__(self,name):
        self.name=name#instance attributes 
    def show(self):
        print(f"Welcome to {self.name}")
        
n=car("Creta")
n.show()

