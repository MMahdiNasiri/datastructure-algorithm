from random_array import random_array


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        node = self.head
        nodes_list = []
        while node is not None:
            nodes_list.append(node.data)
            node = node.next_node
        return nodes_list

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while node.next_node is not None:
                node = node.next_node
            node.next_node = new_node


unsorted_arr = random_array(20, 10000)
print(unsorted_arr)


def radix_sort():
    global unsorted_arr
    max_number = str(max(unsorted_arr))
    for i in range(len(max_number)):
        arr = [None] * 10
        for x in unsorted_arr:
            index = (x // (10**i)) % 10
            if arr[index] is None:
                arr[index] = LinkedList()
            arr[index].insert(x)

        helping_arr = []
        for x in arr:
            if x is not None:
                helping_arr.extend(x.listprint())
        unsorted_arr = helping_arr


radix_sort()
print(unsorted_arr)
