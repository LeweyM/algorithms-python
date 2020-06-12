from unittest import TestCase

from RedBlackTree import RedBlackTree


class TestNode(TestCase):
    def test_tree_legality(self):
        tree = RedBlackTree()
        tree.put(1)
        tree.put(3)
        tree.put(5)

        tree_list = tree.to_list()
        self.assertListEqual(tree_list, [1, 3, 5])

    def test_max_height(self):
        tree = RedBlackTree()
        self.assertEqual(tree.max_height(), 0)
        tree.put(3)
        self.assertEqual(tree.max_height(), 1)
        tree.put(1)
        tree.put(5)
        self.assertEqual(tree.max_height(), 2)

