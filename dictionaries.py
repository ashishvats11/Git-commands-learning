# In this section we will be learning and practice the dictionary - let's Go
# Dictionary stores data in key:value pair. it is ordered(from python 3.7+ onwards), changable and it does not allow duplicates.
# dictionary {k1:v1}

# For easy understanding - dictionary are similar to list in list we have index for each value in the list, same here for each value there is a unique key,



dict1 = {'brand':'Ford','Year':'1997','Model':'Ford Shelby' } # this is a dictionary with key value pairs

print(dict1) # this will print the dictionary
print(f'Accessing the value by passing the key:  {dict1['Year']}') #Accessing the value by passing the keys

dict2 = {'brand':'ParleG', 'year':'2002','product':'Namkeen','year':'2010'} # in this we have passes year two times and dict does not allow duplicate keys
print(dict2['year']) # on running this you will get the last updated value of the year that is 2010

#length of dictionary
print(f'Length of dict2 which has duplicate key (year) {len(dict2)}') #it gave the length as 3 instead of 4 because it only takes on key into account not both'


# the dict() constructor, used to create the dictionaries

# 1 Creating an empty dictionary dict()
empty_dict = dict()
print("This is an empty dictionary",empty_dict)

# 2 From an iterable of key-value pairs: Pass an iterable 
# (like a list or a tuple) containing two-item tuples, where the first item in each tuple is the key and the second is the value.

pairs = [('name','Bob'),('age',23)] # you can  only pass two values as key-value pairs in each () or []
person_dict = dict(pairs)
print(f'Dictionary created from iterabble {person_dict}')

test =[[1,2],[4,5]]
test1 = dict(test)
print(test1)

#3 third way of creating dictionary
p1 = dict(name = 'Ashish',age = 23,salary = 10200201200, country ='India')
print(p1)

# Accessing the dictionary items
cars = dict(brand = 'Audi', year = 2909, model = 'qss69', designed_by = 'Ashish')

# by passing the key name
print(f'Accessing the dictionary element using the key name {cars["brand"]}')

# by using the .get() method
print(f'Accessing the dictionary item using .get(): {cars.get('brand')}')

# .keys() function - return the list of keys in the dictionary
print(f'Using the .keys() we get all the keys in the dictionary: {cars.keys()}')

# .values() - return the list of all the values in the dictionary
print(f'Using the .values() we get all the values in the dictionary: {cars.values()}')

# Update the value of a key

#1 by passing the key name
cars['model'] = 'Q8'
print(f'Dictionary after updating one of the key\'s value {cars}')

#2 by using the update() function - using this function we can update the existing key and even add new key - value pair to the dictionary
cars.update({'year':2025,'closing_year':2300})
print(f'here i have updated the year using the update() function {cars}')

# Adding new item to the dictionary
cars['colour'] = 'Black'
print('Updated dictionary cars with color field added ',cars)

# items() - This method will give each list of items in the dictionary as tuples in a list [(key,value), (key, value)]
print(f'These are the items in the dictionary {cars.items()}')

# Check if key exists in the dictionary
if 'year' in cars:  # this will only work for the keys not the values
    print('This key is present \n')
else:
    print("Sorry, this key is not present \n" )


# Removing the items -- pop(), popitem(), del, clear()

dummy = dict([("name",'Ashish'),("last_name","Vats"),("age",23),("ecode",'q0006919')])
print(f'Dummy dictionary before removing the item {dummy} \n')

# 1st pop() - in this pass the key of the item that we want to remove
dummy.pop('last_name') # in the pop() function we need to pass the key to remove that item
print(f"Dummy dictionary after using the pop() function {dummy}") # we removed the last_name item

# 2nd popitem( )
dummy.popitem() # this function removes the last item of the dictionary and this function doesn't take any argument
print(f'Dummy dictionary after using the popitem() function {dummy}')

# 3rd del keyword - this will delete the item whose key has been passed and it can also delte the whole dictionary
car2 = {'brand':'Audi','year':2025,"price":70000,"color":'black'}
print(car2)
del car2['price']
print(f'The car2 dictionary after deletig the price key item {car2}')

# del car2  -- This will delete the car2 dictionary
# print(car2) --  this will throw car2 not defined error as car2 has been deleted

# clear() -  this will clear all the item inside a dictionary
car2.clear()
print(f'car2 dictionary after using the clear() function {car2}')


# Creating the copy of dictionary
a1 = dict(brand = 'Audi', year = 2002, black = 'Red')
print(a1)
a2 = a1.copy()
print(f'Copy of the a1 dictionary using the copy() function --> {a2}')
a3 = dict(a1)
print(f'Copy of the a1 dictionary using the dict() function --> {a3}')
a1['year'] = 2106
print(f'All the dictionaries after updarting the main dctionary {a1}, {a2}, {a3}')  # you will see only the a1 got changed not the copied ones
