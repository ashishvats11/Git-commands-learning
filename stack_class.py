class Stack:
    def __init__(self): # Constructor
        self.stack = []
    
    def push(self,element):
        self.stack.append(element)
        return self.stack


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

