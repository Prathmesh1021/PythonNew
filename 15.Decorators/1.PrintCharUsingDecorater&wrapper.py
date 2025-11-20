# Use Decorater With Wrapper Function 
# Normaly print the charetores
def decorate(func):
    def wrapper():
        print("i will print myself before the function")
        func()
        print("i will print after the function ")
    return wrapper

@decorate
def hello():
    print("Hello i am Prathmesh Patil")
hello()