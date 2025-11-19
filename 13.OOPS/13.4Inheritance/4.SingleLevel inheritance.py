
#Single level inheritance using 1 parent and 1 child with constructor
class animal:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"hello your name is {self.name}")
class Human(animal):
    pass

person1 =Human("Prathmesh")

animal1=animal("lion")

person1.show()
animal1.show()