#Example of Inheritance Super class SubClass Operation
class FactoryMumbai:# parent Class /super class
    a="I am an attribute mentioned inside Factory "
    def hello (self):
        print("hello I am a metnhod mentioned inside factory")
        
class FactoryPune(FactoryMumbai):#childe class/sub class 
    pass
obj=FactoryMumbai()
obj2=FactoryPune()
obj2.hello()