#Polymorphisam 1 Way Active in paython.#
# Method Overriding 
class Animal:
    def show(self):
        print("Hello I am Prathm")
class Human(Animal):    
    def show(self):
        print("How are You")

obj=Human()
obj.show()
    
        