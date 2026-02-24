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

# Function with parameter in which we define the data type of all parameters we pass in the function
# we achieve this by using the type hints in python 
def teacher (name:str, subject:str,salary:int) -> str:
    return f'Hey {name}, you teach {subject} and your current salary is {salary}'

print(teacher("Ashish","Computer Science",120000)) # type hints are not enforced at run time

# how can we enforce it then? 
def fun(name:str,age:int):
    if not isinstance(age,int):
        raise TypeError("age must be an integer")
    return f'Your name is {name} and age is {age}'
print(fun("Ashish",23))