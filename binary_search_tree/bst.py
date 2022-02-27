class BSTNode:

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def __str__(self):
        return str(self.value)


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, value) -> bool:
        new_node = BSTNode(value)
        if self.root is None:
            self.root = new_node
            return True
        node = self.root
        while True:
            if new_node.value == node.value:
                return False
            if new_node.value < node.value:
                if node.left is None:
                    node.left = new_node
                    return True
                node = node.left
            else:
                if node.right is None:
                    node.right = new_node
                    return True
                node = node.right

    def contains(self, value):
        node = self.root
        while True:
            if node is None:
                return False
            if value == node.value:
                return True
            if value < node.value:
                node = node.left
            else:
                node = node.right

    @staticmethod
    def min_value_node(current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node
