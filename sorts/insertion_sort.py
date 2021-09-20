from random_array import random_array

unsorted_arr = random_array(30)


def insertion_sort(arr):
    for i in range(len(arr)):
        for j in reversed(range(1, i)):
            if arr[j] <= arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    return arr


print(insertion_sort(unsorted_arr))