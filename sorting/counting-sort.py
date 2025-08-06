import random

min_value = 1
max_value = 10
list_size = 10

def countingSort(A):
    locator = [0 for _ in range(max_value + 1)] # init locator array to contain 0 for each element count
    B = [0] + [0 for _ in range(list_size)]

    for i in range(1, list_size + 1): # count the number of each element
        locator[A[i]] += 1

    for x in range(2, max_value + 1): # Set the count at locator[x] to be the sum of every count before it i.e. num of elems <= x
        locator[x] = locator[x] + locator[x-1]

    for i in range(list_size, -1, -1): # traverse backwards
        print(locator, f" index in output for {A[i]} -> {locator[A[i]]}")
        B[locator[A[i]]] = A[i] # place the element at A[i] in the correct position
        locator[A[i]] -= 1
    
    return B

A = [0]+[random.randint(min_value, max_value) for _ in range(list_size)]
print("A:", A)
print("Sorted:", countingSort(A))