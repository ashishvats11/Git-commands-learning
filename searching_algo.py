# Linear Search and Binary Search

arr = [1,2,3,4,5,6,7,8]

# In here we are going to define a function for Linear Search - Time Complexity of linear search is O(n)

def linearSearch(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return f'Value {value} is present in the array at {i} index'
    return 'Given value is not there in the list'

print(linearSearch(arr,9))