class Node:
    def __init__(self, data_val=None):
        self.data_val = data_val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, value):
        new = Node(value)
        new.next = self.head
        self.head = new

    def insert_last(self, value):
        new = Node(value)
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = new

    def insert_middle(self, value, position):
        node = self.head
        new = Node(value)
        if position == 0:
            self.insert_first(value)
        else:
            i = 1
            while i < position and node.next is not None:
                i += 1
                node = node.next
            new.next = node.next
            node.next = new

    def pop(self):
        node = self.head
        if node.next is None:
            self.head = None
            return node.data_val
        while node.next.next is not None:
            node = node.next
        last = node.next
        node.next = None
        return last.data_val

    def key_delete(self, key):
        node = self.head
        while node.next is not None and node.next.data_val != key:
            node = node.next
        if node.next is None:
            return None
        else:
            located_node = node.next
            node.next = located_node.next
            return located_node.data_val

    def print_list(self):
        node = self.head
        while node is not None:
            print(node.data_val)
            node = node.next