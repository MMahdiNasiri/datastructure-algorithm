from random_array import random_array

unsorted_arr = random_array(30)


def bubble_sort(arr):
    for i in range(1, len(arr)):
        for j in range(len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


sorted_arr = bubble_sort(unsorted_arr)

print(sorted_arr)
