
#Accesing Attributes And Methods 
class Animal:
    type="Cat"  #Attributes
    
    def sound(self):#method
        print("Meow!")
        
#diretly accessing attribute and method using the class 
print(Animal().type)
Animal().sound()
