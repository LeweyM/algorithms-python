class QuickSort:
    def __init__(self):
        pass

    def sort(self, arr: list):
        self.q_sort(arr, 0, len(arr) - 1)

    def q_sort(self, arr, lo, hi):
        if lo >= hi:
            return
        # choose a pivot (could just be the first el
        p = partition(arr, lo, hi)
        # repeat recursively on both sides until...
        # comparision of two els.
        self.q_sort(arr, lo, p - 1)
        self.q_sort(arr, p + 1, hi)


def partition(arr: list, lo, hi):
    i = (lo - 1)  # index of smaller element
    pivot = arr[hi]  # pivot

    for j in range(lo, hi):
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
    return i + 1
