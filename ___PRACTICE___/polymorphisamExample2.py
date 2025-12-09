#method overrriding 

class Animal:
    def show(self):
        print("how are you")
class Human(Animal):
     def show(self):
         print("waht abaut you")

obj=Human()
obj.show()