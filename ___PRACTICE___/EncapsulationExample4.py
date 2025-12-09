##Private Example ---Accsess with Class
class Factory:
    __a="this is the private attributes in Ecapsulation"
    def show(self):
        print(Factory().__a)
obj =Factory()
obj.show()