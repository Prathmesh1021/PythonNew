#Duck Example in polymorphisam 
class Animal:
    def show(self):
        print("i am showing")
class Human:
    def show(self):
        print("i am also showing")
        
obj=Animal()
obj2=Human()

obj.show()
obj2.show()