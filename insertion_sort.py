unsorted_arr = [3, 5, 1, 8, 4, 7, 5, 24]


def insertion_sort(arr):
    for i in range(len(arr)):
        for j in reversed(range(1, i)):
            if arr[j] <= arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    return arr


print(insertion_sort(unsorted_arr))