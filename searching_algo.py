# Linear Search and Binary Search

arr = [1,2,3,4,5,6,7,8]

# In here we are going to define a function for Linear Search - Time Complexity of linear search is O(n)

def linearSearch(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return f'Value {value} is present in the array at {i} index'
    return 'Given value is not there in the list'

print(linearSearch(arr,9))


# Now we will learn the Binary Search- for this the array  should be sorted
arr2 = [1,2,3,4,5,6,7,8,9,10]

def binarySearch(array, value):
    l = 0
    h = len(array) - 1
    while(l<=h):
        mid = (l + h)//2
        if array[mid] == value:
            return f'Value {value} is present at {mid} index'
        elif array[mid] > value:
            h = mid - 1
        else:
            l = mid + 1
    return -1
print(f'This is the array that we are going to use for Binary Search {arr2}')

print(binarySearch(arr2,11))
