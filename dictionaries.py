# In this section we will be learning and practice the dictionary - let's Go
# Dictionary stores data in key:value pair. it is ordered(from python 3.7+ onwards), changable and it does not allow duplicates.
# dictionary {k1:v1}

dict1 = {'brand':'Ford','Year':'1997','Model':'Ford Shelby' } # this is a dictionary with key value pairs

print(dict1) # this will print the dictionary
print(f'Accessing the value by passing the key:  {dict1['Year']}') #Accessing the value by passing the keys

dict2 = {'brand':'ParleG', 'year':'2002','product':'Namkeen','year':'2010'} # in this we have passes year two times and dict does not allow duplicate keys
print(dict2['year']) # on running this you will get the last updated value of the year that is 2010

#length of dictionary
print(f'Length of dict2 which has duplicate key (year) {len(dict2)}')