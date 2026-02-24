# In this we will be learning lists []
# List are mutable, can store duplicate values and it's indexing starts from 0. 

#defining list
# A list can be of any type, int, float, string, bool or even mixed data types

lst1 = [1,2,3,4] 
print(f'list of integers {lst1}\n')

lst2 = ['apple','banana','papaya','peach']
print(f'List of strings {lst2}\n')

lst3 = ['apple',1,2,'ashish',2.0]
print(f'List of mixed data type {lst3}\n')

lst4 = [1,1,1,1,1]
print(f'list of dulicates: {lst4}\n')

# accessing the list items, list items are indexed and we can access them by reffering to their index
print(lst3[0])
print(f'negative indexing means starting from the last: {lst3[-2]}\n')

# We can specify the range of indices that we need, the return  value will be a list
print(f'The range of items from the list {lst3[2:5]}\n') # in the range the second value in not inclusive 

#if there is another list in the list
unq = [1,2,3,[4,5,6]] # here the indexing is like [0,1,2,[3][0],[3][1],[3][2]]
print(f'I have accessed the itemm from the list which resides in a list {unq[3][2]}\n')


# If we want to change the value of any particular element of a list
a = [1,2,3,4]
a[1] = 'apple' # over here we are changing the value of element at index 1 i.e 1 to apple
print(a, 'This is the list after change')
a[2:4] = ['Ashish',69.69]
print(f'Here i have changed a range of items {a}\n')


# If we want to remove an element from the list 

#pop()
b = [1,'apple','samsung',5]
b.pop(1) # pop  removes the element that is present on the index passed in the function and if we don't pass any index it will pop the last element of the list
print(b,' this is the list after the element being removed using pop()\n')

b2 = ['A','B','c','A']
b2.remove('A')
print(f'remove(\'A\') removes the first occurence of the element A {b2}')

# del - this also removes the specified index
# del b2[0] -  this will remove the element present at index 0
# del b2 - if we don't specify the index it will delete the whole list

# If we want to append element to the list
c = [1,2,3,4,5]
c.append(6)
print(c, " this is the list after appending the element in the list")

# if we want to append multiple elements to the list - use extend(), this accepts any iterable(something we loop over)
d = [1,2,3]
d.extend("ashish") # we can use any iterable here like string, set, list, tuple
print(d)

# creating list using list()
name = "Ashish"
print(list(name))

# concatenation in list
A = [1,2,3,4]
B = ['A','B','C']
A +=B
print("Concatenated list",A)

# insert(index, value) used to insert an element in the list at a particular index
fruits = ['apple']
fruits.insert(1,'banana')
print(fruits)


# sorting - will sort the list alphanumerically, ascending, by default:
num = [1,3,4,6,10,-1]   
num.sort() # this will sort in ascending order
print(f'This is the sorted list in ascending order: {num}')
num.sort(reverse=True)
print(f'This is sorted in descending order: {num}')
#reverse - reverse the order of a list
num.reverse()
print(f'This is the reversed list {num}')