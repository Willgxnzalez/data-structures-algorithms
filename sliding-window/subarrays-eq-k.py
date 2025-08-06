# Finds all subarrays with sum equal to k

def subarrays_sums_eq_k(array, k):
    sub_arrays = []
    
    left = 0
    current_sum = 0
    for right in range(len(array)):
        current_sum += array[right]
        
        while current_sum > k and left <= right: # If sum exceeds k, remove left most
            current_sum -= array[left]
            left += 1
            
        if current_sum == k:
            sub_arrays.append(array[left:right+1])
    return sub_arrays

array = [1,6,2,31,1,8]
k = 9
print(array, f'k = {k}')
sub_arrays = subarrays_sums_eq_k(array, k)
print(sub_arrays, len(sub_arrays))
        