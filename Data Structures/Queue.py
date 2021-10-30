from LinkedList import Node, LinkedList


class QueueWithList:
    def __init__(self):
        self.queue = []

    def push(self, value):
        self.queue.append(value)

    def pop(self):
        return self.queue.pop(0)


class QueueWithLinkedList:
    def __init__(self):
        self.queue = LinkedList()

    def push(self, value):
        self.queue.insert_first(value)

    def pop(self):
        return self.queue.pop()