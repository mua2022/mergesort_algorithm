import time
import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

# Generate a random array of size 10000
arr = random.sample(range(10**6), 10000)

# Print the original array
print("Original array:", arr)

# Measure the time taken to sort the array
start_time = time.time()
sorted_arr = merge_sort(arr)
end_time = time.time()

# Print the sorted array
print("Sorted array:", sorted_arr)

# Print the time taken to sort the array
print("Time taken to sort the array:", end_time - start_time, "seconds")