#Multiple inheritance 2parent 1child
class Animal:
    def __init__(self,name):
        pass
class Human:
    def __init__(self,name,age):
        pass
   
class Roborts(Human,Animal):
    name3="Charli777"

obj=Roborts()