from random_array import random_array

unsorted_arr = random_array(20)
print(unsorted_arr)

def merge_sort(start, end):
    if end - start <= 1:
        return
    else:
        middle = start + int((end - start)/2)
        merge_sort(start, middle)
        merge_sort(middle, end)
        arr = list()
        i = start
        j = middle
        while i < middle or j < end:
            if j < end and unsorted_arr[j] < unsorted_arr[i]:
                arr.append(unsorted_arr[j])
                j += 1
            elif i < middle:
                arr.append(unsorted_arr[i])
                i += 1
            else:
                arr.append(unsorted_arr[j])
                j += 1
        for i in range(len(arr)):
            unsorted_arr[start+i] = arr[i]


merge_sort(0, len(unsorted_arr))
print(unsorted_arr)


def merge(arr):
    if len(arr) < 2:
        return arr
    else:
        arr1 = merge(arr[:len(arr)//2])
        arr2 = merge(arr[len(arr)//2:])
        i = 0
        j = 0
        sorted_arr = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                sorted_arr.append(arr1[i])
                i += 1
            else:
                sorted_arr.append(arr2[j])
                j += 1
        while i < len(arr1):
            sorted_arr.append(arr1[i])
            i += 1

        while j < len(arr2):
            sorted_arr.append(arr2[j])
            j += 1
        return sorted_arr
