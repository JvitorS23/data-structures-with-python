class DoublyLinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


class DoublyLinkedList:

    def __init__(self, value=None):
        node = None
        self.length = 0
        if value:
            node = DoublyLinkedListNode(value)
            self.length = 1
        self.head = node
        self.tail = node
        self.reverse = False

    def __str__(self):
        node = self.head
        attr = 'next'
        if self.reverse:
            node = self.tail
            attr = 'prev'
        str_ll = ''
        while node is not None:
            str_ll += f'{node.value} '
            node = node.__getattribute__(attr)
        return str_ll

    def is_empty(self):
        return self.length == 0

    def append(self, value):
        new_node = DoublyLinkedListNode(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = DoublyLinkedListNode(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop(self):
        if self.is_empty():
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            popped_node.prev = None
        self.length -= 1
        return popped_node

    def pop_first(self):
        if self.is_empty():
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            popped_node.next = None
        self.length -= 1
        return popped_node

    def get(self, index):
        if index < 0 or index > self.length:
            return None
        if index < self.length / 2:
            node = self.head
            for _ in range(index):
                node = node.next
        else:
            node = self.tail
            for _ in range(self.length - 1, index, -1):
                node = node.prev
        return node

    def set_value(self, index, value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = DoublyLinkedListNode(value)
        previous_node = self.get(index - 1)
        after_node = previous_node.next

        new_node.prev = previous_node
        new_node.next = after_node
        after_node.prev = new_node
        previous_node.next = new_node

        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        removed_node = self.get(index)
        previous_node = removed_node.prev
        after_node = removed_node.next

        previous_node.next = after_node
        after_node.prev = previous_node

        removed_node.next = None
        removed_node.prev = None

        self.length -= 1
        return True
