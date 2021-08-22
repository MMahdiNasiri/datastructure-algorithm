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
