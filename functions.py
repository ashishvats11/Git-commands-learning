# in this we will be learning about python functions

#define function - def is the keyword to define function

def function():
    print("Hello, welcome to your first function")

#invoking/calling the function
function() # this will call the function and will print the statement inside the function

#function with parameters 
def student(name,age,grade):
    return f'I am {name} and I am {age} years old and Study in class {grade}'
print(student('Ashish',23,'2nd')) # in here we had to print the function because we were returning the result instead of printing inside the function