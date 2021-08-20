from random_array import random_array

unsorted_arr = random_array(30)


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
            if i < middle and unsorted_arr[i] < unsorted_arr[j]:
                arr.append(unsorted_arr[i])
                i += 1
            elif j < end:
                arr.append(unsorted_arr[j])
                j += 1
        print(arr)
        for i in range(len(arr)):
            unsorted_arr[start+i] = arr[i]


merge_sort(0, len(unsorted_arr))
print(unsorted_arr)
