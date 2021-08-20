import random


def random_array(num):
    unsorted_arr = []
    for x in range(num):
        unsorted_arr.append(random.randint(0, num))

    return unsorted_arr
