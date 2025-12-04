#creating stack using class 
class Stack:
    def __init__(self):
        self.stack=[]
    
    def push(self,element):
        self.stack.append(element)
        
    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack)==0
    
    
    def size(self):
        return len(self.stack)
    
mystack=Stack()
mystack.push('A')
mystack.push('B')
mystack.push('C')


print("Stack :",mystack.stack)
print("Pop :",mystack.pop())
print("After Pop Stack is :",mystack.stack)
print("Peek: ",mystack.peek())
print("Empty :",mystack.isEmpty())
print("Size :",mystack.size())
