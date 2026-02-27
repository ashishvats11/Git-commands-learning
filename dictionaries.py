# In this section we will be learning and practice the dictionary - let's Go
# Dictionary stores data in key:value pair. it is ordered(from python 3.7+ onwards), changable and it does not allow duplicates.
# dictionary {k1:v1}



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
cars['model'] = 'Q8'
print(f'Dictionary after updating one of the key\'s value {cars}')

# Adding new item to the dictionary
cars['colour'] = 'Black'
print('Updated dictionary cars with color field added ',cars)

# items() - This method will give each list of items in the dictionary as tuples in a list [(key,value), (key, value)]
print(f'These are the items in the dictionary {cars.items()}')

# Check if key exists in the dictionary
if 'year' in cars:  # this will only work for the keys not the values
    print('This key is present')
else:
    print("Sorry, this key is not present")