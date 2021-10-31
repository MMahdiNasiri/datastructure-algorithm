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
        if position == 0:
            self.insert_first(value)
        else:
            node = self.head
            new = Node(value)
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


class DoublyNode(Node):
    def __init__(self, data_val=None):
        Node.__init__(self, data_val)
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, value):
        new_node = DoublyNode(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_last(self, value):
        new_node = DoublyNode(value)
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = new_node
        new_node.prev = node

    def insert_middle(self, value, position):
        if position == 0:
            self.insert_first(value)
        else:
            node = self.head
            new = DoublyNode(value)
            i = 1
            while i < position and node.next is not None:
                i += 1
                node = node.next

            new.next = node.next
            new.prev = node
            node.next = new
            new.next.prev = new

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
            if located_node.next is not None:
                located_node.next.prev = node
            return located_node.data_val

    def print_list(self):
        node = self.head
        while node is not None:
            next_val = node.next.data_val if node.next is not None else None
            prev_val = node.prev.data_val if node.prev is not None else None
            print('node ', node.data_val, ', prev: ', prev_val, ', next: ', next_val)
            node = node.next
