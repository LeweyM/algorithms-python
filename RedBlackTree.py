BLACK = 0
RED = 1


class Node:
    def __init__(self, value, color):
        self.left = None
        self.right = None
        self.value = value
        self.color = color


def put_recur(value: int, node: Node):
    if node is None:
        return Node(value, RED)

    node.left = put_recur(value, node.left)
    return node


class RedBlackTree:
    def __init__(self):
        self.root = None

    def put(self, value: int):
        self.root = put_recur(value, self.root)

    def to_list(self):
        queue = []
        result = []
        node = self.root
        if node is None:
            return []

        queue.append(self.root)
        while len(queue) > 0:
            curr = queue.pop(0)
            result.append(curr.value)
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)

        return result
