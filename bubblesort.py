unsorted_arr = [3, 5, 1, 8, 4, 7, 5, 24]


def bubble_sort(arr):
    for i in range(1, len(arr)):
        for j in range(len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


sorted_arr = bubble_sort(unsorted_arr)

print(sorted_arr)
