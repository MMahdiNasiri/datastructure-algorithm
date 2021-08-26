from random_array import random_array


unsorted_arr = random_array(20, 10000)
print(unsorted_arr)


def counting_sort(digit_num):
    global unsorted_arr
    arr = [0] * 10
    helping_arr = []
    for i in range(len(unsorted_arr)):
        index = (unsorted_arr[i] // (10 ** digit_num)) % 10
        arr[index] += 1

    for i in range(10):
        for j in unsorted_arr:
            if arr[i] < 1:
                break
            if ((j // (10 ** digit_num)) % 10) == i:
                helping_arr.append(j)
                arr[i] -= 1
    unsorted_arr = helping_arr


def radix_sort():
    n = str(max(unsorted_arr))
    for i in range(len(n)):
        counting_sort(i)
    print(unsorted_arr)


radix_sort()
