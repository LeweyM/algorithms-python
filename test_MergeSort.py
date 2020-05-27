import unittest
from unittest import TestCase
from MergeSort import MergeSort
from QuickSort import QuickSort

if __name__ == '__main__':
    unittest.main()


class TestMerge(TestCase):
    def setUp(self):
        self.merge_sort = MergeSort()
        self.quick_sort = QuickSort()


def sort_orders_correctly(sorter):
    x, y = get_sorted_lists(sorter)
    return x == y


def get_sorted_lists(sorter):
    x = [5, 2, 3, 6, 7, 1, 2, 6, 31, 12, 432, 2, 52, 65, 56, 1, 5, 2, 3, 3, 3, 3, 3]
    y = x.copy()
    y.sort()
    sorter.sort(x)
    return y, x


class TestInit(TestMerge):
    def test_sorts(self):
        x, y = get_sorted_lists(self.merge_sort)
        self.assertEqual(x, y)


class TestQuickSort(TestMerge):
    def test_quick_sort(self):
        x, y = get_sorted_lists(self.quick_sort)
        self.assertEqual(x, y)

