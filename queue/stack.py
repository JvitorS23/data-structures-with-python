class QueueNode:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class Queue:

    def __init__(self, value=None):
        node = None
        self.length = 0
        if value:
            node = QueueNode(value)
            self.length = 1
        self.first = node
        self.last = node

    def __str__(self):
        node = self.first
        str_stack = ''
        while node is not None:
            str_stack += f'{node.value} '
            node = node.next
        return str_stack

    def is_empty(self):
        return self.length == 0

    def enqueue(self, value):
        new_node = QueueNode(value)
        if self.is_empty():
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.is_empty():
            return None
        first_node = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            first_node.next = None
        self.length -= 1
        return first_node


mq = Queue(1)
mq.enqueue(2)
mq.enqueue(3)
print(mq)
mq.dequeue()
print(mq)

mq.dequeue()
print(mq)

mq.dequeue()
print(mq)

