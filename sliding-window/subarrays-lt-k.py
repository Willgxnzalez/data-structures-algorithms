# find number of subarrays with sum less than K

def subarrays_sums_lt_k(array, K):
    sub_arrays = []
    left = 0
    current_sum = 0
    
    for right in range(len(array)):
        current_sum += array[right]
        
        # Shrink the window if the sum exceeds K
        while current_sum >= K and left <= right:
            current_sum -= array[left]
            left += 1
        
        # For every valid window, collect all subarrays ending at `right`
        for i in range(left, right + 1):
            sub_arrays.append(array[i:right + 1])
    return sub_arrays

array = [1,6,2,31,1,6]
k = 9
print(array, f'k = {k}')
sub_arrays = subarrays_sums_lt_k(array, k)
print(sub_arrays, len(sub_arrays))