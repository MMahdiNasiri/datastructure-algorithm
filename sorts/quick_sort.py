from random_array import random_array

unsorted_arr = random_array(30)


def quick_sort(arr):
    if len(arr) <= 1:
        print(arr)
        return arr
    else:
        i = 0
        j = len(arr) - 1
        p = 0
        while i < j:
            while arr[j] > arr[p] and i < j:
                j -= 1
            while arr[i] <= arr[p] and i < j:
                i += 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[p], arr[i] = arr[i], arr[p]
        print(arr)
        return quick_sort(arr[:j]) + arr[j:j + 1] + quick_sort(arr[j + 1:])


def quicksort(start, end):
    length = end - start
    print(end, start, length)
    if length <= 1:
        print('in if')
        return
    i = start
    j = end-1
    p = start
    while i < j:
        while unsorted_arr[j] > unsorted_arr[p] and i < j:
            j -= 1
        while unsorted_arr[i] <= unsorted_arr[p] and i < j:
            i += 1
        if i < j:
            unsorted_arr[i], unsorted_arr[j] = unsorted_arr[j], unsorted_arr[i]
    unsorted_arr[p], unsorted_arr[i] = unsorted_arr[i], unsorted_arr[p]
    quicksort(start, i)
    quicksort(i+1, end)


# sorted = quick_sort(unsorted_arr)
quicksort(0, len(unsorted_arr))
print(unsorted_arr)
