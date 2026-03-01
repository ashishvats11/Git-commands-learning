# Loops in Dictionary -  
dict1 = dict(name ='Ashish',age = 23, last_name = 'vats')
print(dict1)

for i in dict1:  # when looping through a dictionary, the return values are the keys but there are some methods to access the values 
    print(i, end=', ') 
print() 

# using the .keys() method to return the keys of the dictionary

# printing the values 
print(f'These are the values ', end = ':')
for i in dict1:
    print(dict1[i], end=',')
print()

# using the .values() to return the values of the dictionary 
for i in dict1.values():
    print(i,end=' ')
print()
# to loop through both keys and values
for i in dict1.items():
    print(i)

# 2nd way 
for i, j  in dict1.items(): # in this way we access keys and values separately as they are being stored in variables i and j respectively
    print(i,j)


   
