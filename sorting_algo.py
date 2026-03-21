# In this we will learn different Ssorting Algorithms

# 1. Bubble Sort - Basic sorting Algorithm

a= [0, 1, 2, 2, 3, 5, 6, 8, 10, 19]
def bubbleSort(array):
    n = len(array)
    for i in range(len(array)-1):
        swapped = False
        for j in range(0,n - i -1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
                swapped = True
        if not swapped:
            break
    return array

print(f'Bubble Sort - {bubbleSort(a)}')
b = [8,4,3,1,6,2,0,1]
print(f'Bubble Sort {bubbleSort(b)}')

# 2. Selection Sort - In this we find the smallest number and bring it to the starting of the array(by swapping)
def selectionSort(array):
    n = len(array)
    for i in range(n):
        min_value = array[i]
        min_index = i
        for j in range(i+1, n):
            if array[j] < min_value:
                min_value = array[j]
                min_index = j  
        array[i],array[min_index] = array[min_index],array[i]
      
    return array

print(f'Selection Sort {selectionSort(b)}')