# In this we will be looking at Stacks in python
# Push, peek, popm isEmpty, size

stack = [] #  empty stack

# Push operartin in stack
stack.append('A')
stack.append('B')
stack.append('C')
stack.append('D')
print(f'Stack: {stack}')

# Peek operation in stack
topelement =stack[-1]
print(f'Top element of the stack: {topelement}')

# Pop the top element
poppedElement = stack.pop()
print(f"Popped element of the stack: {poppedElement}")

#Stack after popping the top element
print(f'Stack after popping the top element: {stack}')

#isEmpty
isEmpty = not bool(stack)
print("isEmpty", isEmpty)

if stack: # It checks if stack is non-empty(True) or empty(False)
    print('Stack is not empty')
else:
    print('Stack is empty')

# Size of the stack 
print(f'Size of the stack: {len(stack)}')