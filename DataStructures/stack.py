from .LinkedList import Node, LinkedList


class StackWithList:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return bool(len(self.stack))


class StackWithLinkedList:
    def __init__(self):
        self.link_list = LinkedList()

    def push(self, value):
        self.link_list.insert_last(value)

    def pop(self):
        return self.link_list.pop()

    def is_empty(self):
        return self.link_list.head is None
