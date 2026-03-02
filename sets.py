# In this we will be learning about the Sets
# Sets are represented as {}
# Sets are one of the 4 data types used to store collections of data
# A set is a collection which is unordered, unchangeable*, and unindexed.
# Set items are unchangeable  but we can add and remove the set items

# Sets does not allow duplicates - a set  can not have duplicate values. Even if you provide duplicates it will only consider them as one in the list

# Creating a set
a1 = {1,2,3,4}
print(a1, type(a1))

# Set does not allow duplicates
a2 = {1,2,3,3,4,5,6,6}
print(f'In this set i have given duplicate values but it will consider only one {a2}') # it takes only unique value

# True and 1 are considered the same in sets same with False and 0
a3  = {1,2,True,3,"Apple",False,0}
print(f'In this set I have passed diff data types of elements {a3}') 

print(f'Length of the a3 set {len(a3)}') # this will give the length of the set after removing the duplicates from the set

# Set() constructor to create a set 
# Pass any iterable in the set() constructor it will convert it into sets
a4 = set((1,2,3,4)) # passed tuple
a5 = set(['apple','banana']) # passed list
a6 = set('String') # passed string
a7 = set({1,2,3,4,5,2}) # passed set

#converting a dictionary into sets
d1 = {'first_name':'Ashish','last_name':'Vats','age':23}

a8 = set(d1) # Dictionary passed - in this the set will only have keys
a9 = set(d1.values()) # This will make a set of dictionary values
a10 = set(d1.items()) # This will make a set of key_value pairs of dictionary
print(f'Set a4: {a4} and set a5: {a5} and set a6: {a6} and set a7: {a7}')
print(f'set a8 from a dictionary (only  keys): {a8}') # In this the set will have the keys of the dictionary
print(f'set a9 from a dictionary (only values): {a9}') # In this the set will have the values of the dictionary
print(f'Set a10 from a dictionary (items -  key:value) {a10}') # in this the set will have the key value pair of the dictionary


# Access set items
# access using the for loop
print('Items in the a3 set: ' , end=': ') 
for i in (a3):
    print(i, end= ' ')
print()

#Check if items are in the sets
print('Apple' in a3)
print('Apple' not in a3)
print('Pine' in a3)

# Add items in the set
# Once a set is created you can not change it, but we can add and remove the elements in a set
# we have .add() and .update() methods

# 1 .add() -  This method only takes one argument
set1 = {'Ashish', 'Vats', 23,'Data'}
set1.add('Data Engineer')
print(set1)

#2 .update() - this allows us to add multiple values in the set
# In this we pass an iterable object - list, tuple, dictionary, strings, sets
set1.update('Happy') # this will add the characters of string in the set as string is an iterable object
print(f'Passing string in the update() {set1}')

set1.update({1,2,3}) # passing the set
print(f'Passing set in the update() {set1}')

# Passing the dictionary in the Sets
dict1 = {'name':'Apple','age':'thirty six'}
# set1.update(dict1.values()) # this will add the values in the set
# set1.update(dict1.items()) # In this the set will have the key value pair of the dictionary - tuples of key value pair
set1.update(dict1) # this will add the keys in the set
print(f'Passing dictionary in the update() {set1}')


# Remove the items of a set -  remove(),  discard(), pop(), clear() and del

test1 = {'apple', 'banana','watermelon', 'Beries', 'Kiwi', 'Pineapple'}
print(f'The original set test1: {test1}')

# remove() - Pass the value of the item in the set that we want to remove. If that item isn't there in the list it will throw an error
test1.remove('apple')
print(f'The test1 set after removing the apple using remove() {test1} ')

# discard() - It works same as remove() but it DOES NOT throw an error if the element that we are removing is not present in the set
test1.discard(12)
print(f'We passed an element which is not there in the set but this time we used discard() {test1}') 

#pop() - This method removes any item from the set
test1.pop()
print(f'the test1 set after using the pop() {test1}')

# clear() - this function will empty the set
test1.clear()
print(f'The clear() {test1}')

# del keyword - this will delete the set
# del test1
# print(f'Test1 set after using the del keyword {test1}') -- It will throw an error because test1 has been deleted


## Join Sets ##

s1 = {'a','b','v'}
s2 = {1,2,3,5,65}
s3 = {'apple','banana'}
print(f'Union of sets {s1 | s2}')
print(f'Union of multiple sets {s1.union(s2,s3)}') # s1|s2|s3

## Intersection of sets

a = {'apple','banana','cherry','melon','blackberry'}
b = {'apple','microsoft','google','blackberry'}
c = {'banana','cherry','blackberry'}
print(f'Intersection of two sets {a & b}')
print(f'Intersection of multiple sets {a.intersection(b,c)}') # a&b&c 

## Difference of sets - # contain only the items from the first set that are not present in the other set.
a1 = {1,2,3,4}
a2 = {2,3,5,6,7}
print(f'Difference of two sets { a1.difference(a2)}') # a1 - a2 , Multiple sets are also allowed

# Symmetric Difference - method will keep only the elements that are NOT present in both sets.

b1 = {"apple", "banana", "cherry"}
b2 = {"google", "microsoft", "apple"}

print(f'Symmetric differene of two sets {b1.symmetric_difference(b2)}')
