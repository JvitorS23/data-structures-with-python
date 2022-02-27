class StackNode:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class Stack:

    def __init__(self, value=None):
        node = None
        self.height = 0
        if value:
            node = StackNode(value)
            self.height = 1
        self.top = node

    def __str__(self):
        node = self.top
        str_stack = ''
        while node is not None:
            str_stack += f'{node.value}\n'
            node = node.next
        return str_stack

    def is_empty(self):
        return self.height == 0

    def push(self, value):
        new_node = StackNode(value)
        new_node.next = self.top
        self.top = new_node
        self.height += 1
        return True

    def pop(self):
        if self.is_empty():
            return None
        popped_node = self.top
        self.top = self.top.next
        popped_node.next = None
        self.height -= 1
        return popped_node
