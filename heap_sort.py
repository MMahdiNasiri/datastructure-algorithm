from random_array import random_array

unsorted_arr = random_array(10)

print(unsorted_arr)


def heapify(i, n):
    left = i * 2 + 1
    right = i * 2 + 2
    maximum = i
    if left < n and unsorted_arr[maximum] < unsorted_arr[left]:
        maximum = left

    if right < n and unsorted_arr[maximum] < unsorted_arr[right]:
        maximum = right

    if maximum != i:
        unsorted_arr[maximum], unsorted_arr[i] = unsorted_arr[i], unsorted_arr[maximum]
        heapify(maximum, n)


def heap_sort():
    n = len(unsorted_arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(i, n)

    for i in range(n-1, 0, -1):
        unsorted_arr[0], unsorted_arr[i] = unsorted_arr[i], unsorted_arr[0]
        heapify(0, i)


heap_sort()
print(unsorted_arr)
