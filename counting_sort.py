from random_array import random_array

unsorted_arr = random_array(30)


def counting_sort(arr):
    count_arr = [0] * (max(arr) + 1)
    sorted_arr = list()
    for i in arr:
        count_arr[i] += 1
    for i in range(len(count_arr)):
        while count_arr[i]:
            sorted_arr.append(i)
            count_arr[i] -= 1
    return sorted_arr


print(counting_sort(unsorted_arr))
