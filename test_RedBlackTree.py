from unittest import TestCase

from RedBlackTree import RedBlackTree, BLACK, RED


class TestTree(TestCase):
    def setUp(self):
        self.tree = RedBlackTree()


class TestNode(TestTree):
    def test_tree_legality(self):
        self.tree.put(3)
        self.tree.put(1)
        self.tree.put(5)

        tree_list = self.tree.to_list()
        self.assertListEqual(tree_list, [3, 1, 5])

    def test_max_height(self):
        self.assertEqual(self.tree.max_height(), 0)
        self.tree.put(3)
        self.assertEqual(self.tree.max_height(), 1)
        self.tree.put(1)
        self.tree.put(5)
        self.assertEqual(self.tree.max_height(), 2)

    def test_left_rotate(self):
        self.tree.put(3)
        self.tree.put(1)
        self.tree.put(5)
        self.tree.put(6)
        self.tree.put(4)
        self.tree.root.color = BLACK
        self.tree.root.left.color = BLACK
        self.tree.root.right.color = RED
        self.assertListEqual(self.tree.to_list(), [3, 1, 5, 4, 6])
        #   3b
        # 1b   5r
        #     4 6
        self.tree.root = self.tree.root.left_rotate()
        #     5b
        #   3r   6
        #  1 4
        self.assertListEqual(self.tree.to_list(), [5, 3, 6, 1, 4])
        self.assertEqual(self.tree.root.color, BLACK)
        self.assertEqual(self.tree.root.left.color, RED)

    def test_right_rotate(self):
        self.tree.put(4)
        self.tree.put(2)
        self.tree.put(6)
        self.tree.put(1)
        self.tree.put(3)
        self.tree.root.color = BLACK
        self.tree.root.left.color = RED
        self.tree.root.right.color = BLACK
        self.assertListEqual(self.tree.to_list(), [4, 2, 6, 1, 3])
        #     4
        #  2     6
        # 1 3
        self.tree.root = self.tree.root.right_rotate()
        #     2
        #  1     4
        #       3 6
        self.assertListEqual(self.tree.to_list(), [2, 1, 4, 3, 6])
        self.assertEqual(self.tree.root.color, BLACK)
        self.assertEqual(self.tree.root.right.color, RED)

    def test_flip_colors(self):
        self.tree.put(3)
        self.tree.put(1)
        self.tree.put(5)
        self.tree.root.color = BLACK
        self.assertTrue(self.tree.root.color == BLACK)
        self.assertTrue(self.tree.root.left.color == RED)
        self.assertTrue(self.tree.root.right.color == RED)

        self.tree.root.flip_colors()

        self.assertTrue(self.tree.root.color == RED)
        self.assertTrue(self.tree.root.left.color == BLACK)
        self.assertTrue(self.tree.root.right.color == BLACK)
