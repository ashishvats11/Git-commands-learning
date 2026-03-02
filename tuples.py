# In this we will be learning about the tuples
# Tuples - ()
# Tuples are immutable 
# Tuple  is a collection which are Ordered and Unchangeable and allow duplicate values
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
# Tuple can store different data types in a single tuple

thistuple = ('apple','banana','cherry',5,True)
print(f'The first ever tuple: {thistuple}')
print(f'Length of the tuple {len(thistuple)}')

# Tuple  with one item
t1 = ("apple",) # To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
print(f'Tuple with one item {t1} and it\'s type is {type(t1)}')

# tuple() constructor 
t2 = tuple(('apple',1,True))
print(f'tuple created using the tuple() constructor {t2}')

# Access the tuple elements

# 1 using the index
print(f'Accessing the tuple element using the index {thistuple[2]}')

# 2 Using negative index 
print(f'Accessing the tuple element using the negative index {thistuple[-1]}')

# 3 Using the Range of Index [x:y] - here x and y are indexes and y is not included here
print(f'Accessing the tuple element using range of indexes {thistuple[1:4]}')

# 4 Using the negative range of index
print(f'Accessing the set elements using negative range of indexes {thistuple[-3:-1]}')

# Membership operator - in
if True in thistuple:
    print('Yes it\'s there')

# Unpack a Tuple
fruits = ('apple','banana','blueberry','strawberry','rasberry')
(green,yellow,blue,red,magenta) = fruits 
print("Unpacked the items in the fruits")
print(green)
print(yellow)
print(blue)
print(red)
print(magenta)
(green,*favs, rich) = fruits
print('In this we have done the unpacking using the asterisk:')
print(green)
print(favs) # stores in list
print(rich)


