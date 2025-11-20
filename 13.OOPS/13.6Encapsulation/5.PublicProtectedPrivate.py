#Program for Public Protected Private Access 
class Demo:
    def __init__(self):
        self.name="publicmember"#Public
        self._age=21        #Protected
        self.__Salary=50000 #Private 
        
    def show(self):
        print("Inside The Class:")
        print("publics",self.name)
        print("protected:",self._age)
        print("private",self.__Salary)
        
obj=Demo()
obj.show()