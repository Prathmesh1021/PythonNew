# Use Decorator for Sum of Two or More Numbers using Wrapper Method 

def decorate(func):
    def wrapper(a,b):
        print("The Addition of two Numbers are ")
        func(a,b)
        print("Thank you! i hope you liked it")
    return wrapper

@decorate
def addition(a,b):
    print(f"total addition is : {a+b}")
addition(21,34)