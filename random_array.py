import random


def random_array(num, maxnum=None):
    if maxnum is None:
        maxnum = num
    unsorted_arr = []
    for x in range(num):
        unsorted_arr.append(random.randint(0, maxnum))

    return unsorted_arr
