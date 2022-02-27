class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:

    def __init__(self, value=None):
        node = None
        self.length = 0
        if value:
            node = LinkedListNode(value)
            self.length = 1
        self.head = node
        self.tail = node

    def __str__(self):
        node = self.head
        str_ll = ''
        while node is not None:
            str_ll += f'{node.value} '
            node = node.next
        return str_ll

    def is_empty(self):
        return self.length == 0

    def append(self, value):
        node = LinkedListNode(value)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = LinkedListNode(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head
        previous = self.head
        while temp.next is not None:
            previous = temp
            temp = temp.next
        self.tail = previous
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def pop_first(self):
        if self.is_empty():
            return None
        first_node = self.head
        self.head = self.head.next
        first_node.next = None
        self.length -= 1
        if self.is_empty():
            self.tail = None
        return first_node

    def get(self, index):
        if index < 0 or index > self.length:
            return None
        node = self.head
        for _ in range(index):
            node = node.next
        return node

    def set_value(self, index, value) -> bool:
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value) -> bool:
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = LinkedListNode(value)
        previous_node = self.get(index - 1)
        new_node.next = previous_node.next
        previous_node.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        previous_node = self.get(index - 1)
        if not previous_node:
            return None
        removed_node = previous_node.next
        previous_node.next = removed_node.next
        removed_node.next = None
        self.length -= 1
        return removed_node

    def reverse(self):
        if self.is_empty() or self.length == 1:
            return
        before = None
        current = self.head
        self.head = self.tail
        self.tail = current
        for _ in range(self.length):
            after = current.next
            current.next = before
            before = current
            current = after
