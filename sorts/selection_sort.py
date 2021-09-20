from random_array import random_array

unsorted_arr = random_array(30)


def selection_sort(arr):
    for i in range(len(arr)):
        flag = i
        for j in range(i, len(arr)):
            if arr[j] < arr[flag]:
                flag = j
        arr[flag], arr[i] = arr[i], arr[flag]
    return arr


print(selection_sort(unsorted_arr))
