class Stack:
    def __init__(self): # Constructor
        self.stack = []
    
    def push(self,element):
        self.stack.append(element)
        

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return f"The stack is empty"

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:return f'The stack is empty'

    def isEmpty(self):
        return not bool(self.stack)

    def size(self):
        return len(self.stack)

# If you want to import this class in another file
# from stack_class import Stack

stack1 = Stack()

stack1.push(1)
stack1.push('Apple')
print(stack1.stack)
print(stack1.peek())
print(stack1.pop())
print(stack1.size())