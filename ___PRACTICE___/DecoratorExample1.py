def decorate(func):
    def Wrapper():
        print("befotr ")
        func()
        print("after")
    return Wrapper

@decorate
def hello():
    print("hello i am prathmesh patil")
hello()
    
    