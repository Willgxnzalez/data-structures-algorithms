import random
from insertionSort import insertion_sort

list_size = 10
min_value = 0.00
max_value = 0.99

def bucketSort(A):
    buckets = [[] for _ in range(list_size)]
    for i, x in enumerate(A):
        buckets[round(A[i]*list_size) - 1].append(x)
    print(buckets)

A = [round(random.uniform(0.00, 0.99), 2) for _ in range(list_size)]
print(A)
print(bucketSort(A))