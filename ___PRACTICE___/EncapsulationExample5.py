class Demo:
    def __init__(self):
         self.name="Public member"
         self._age=21
         self.__Salary=50000
    def show(self):
        print("Inside The Class")
        print("name",self.name)
        print("age",self._age)
        print("Salary",self.__Salary)
        
obj=Demo()
obj.show()