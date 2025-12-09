#Duck Typing

class Animal:
    def show(self):
        print("i am showing")
class Human:
    def show(self):
        print("i am also showing")
        
obj=Animal()
obj1=Human()

obj.show()
obj1.show()