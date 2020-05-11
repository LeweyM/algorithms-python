from unittest import TestCase

from MergeSort import MergeSort


class TestMerge(TestCase):
    def setUp(self):
        self.merge_sort = MergeSort()


class TestInit(TestMerge):
    def test_sorts(self):
        x = [5, 2, 3, 6, 7, 1, 2, 6, 31, 12, 432, 2, 52, 65, 56, 1, 5, 2, 3]
        y = x.copy()

        y.sort()
        self.merge_sort.sort(x)

        self.assertEqual(x, y)
