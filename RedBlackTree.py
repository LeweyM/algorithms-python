BLACK = 0
RED = 1


class Node:
    def __init__(self, value, color):
        self.left = None
        self.right = None
        self.value = value
        self.color = color

    def left_rotate(self):
        x = self.right
        self.right = x.left
        x.left = self
        x.color = self.color
        self.color = RED
        return x

    def right_rotate(self):
        x = self.left
        self.left = x.right
        x.right = self
        x.color = self.color
        self.color = RED
        return x

    def flip_colors(self):
        assert(self.color == BLACK)
        assert(self.left.color == RED)
        assert(self.right.color == RED)
        self.color = RED
        self.left.color = BLACK
        self.right.color = BLACK


class RedBlackTree:
    def __init__(self):
        self.root = None
        self.longest_height = 0

    def put(self, value: int):
        self.root = self.put_recur(value, self.root, 1)

    def put_recur(self, value: int, node: Node, height):
        if node is None:
            self.longest_height = max(self.longest_height, height)
            return Node(value, RED)
        if value < node.value:
            node.left = self.put_recur(value, node.left, height + 1)
        else:
            node.right = self.put_recur(value, node.right, height + 1)
        return node

    def max_height(self):
        return self.longest_height

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
