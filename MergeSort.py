from typing import List


def merge(first_half, second_half):
    i = 0
    j = 0
    # merge sort in place is complicated, so we create a new buffer to store the return.
    res = []
    while True:
        # if one list has been fully added to the buffer, add the rest of the other list
        if i >= len(first_half):
            res += second_half[j:]
            return res
        if j >= len(second_half):
            res += first_half[i:]
            return res
        # add the smallest of the two pointer values and increment the one we select.
        if first_half[i] < second_half[j]:
            res.append(first_half[i])
            i += 1
        else:
            res.append(second_half[j])
            j += 1


class MergeSort:

    def __init__(self):
        pass

    def sort(self, a: List):
        # split the list into two sub-lists
        # duplicating to two new arrays, so not very memory efficient
        first_half = a[:len(a) // 2]
        second_half = a[len(a) // 2:]

        # recurse until there is only two sublists of one element.
        # An optimization here would be to use insertion sort for small sublists.
        if len(first_half) > 1 or len(second_half) > 1:
            self.sort(first_half)
            self.sort(second_half)

        a[:] = merge(first_half, second_half)
