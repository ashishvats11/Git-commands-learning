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

print(bubbleSort(a))
b = [8,4,3,1,6,2,0]
print(bubbleSort(b))

