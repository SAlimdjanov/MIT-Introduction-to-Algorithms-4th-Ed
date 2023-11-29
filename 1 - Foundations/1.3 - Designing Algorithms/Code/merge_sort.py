"""
merge_sort.py

"""

from math import floor


def merge(array, start, midpoint, end):
    """Merging procedure

    Args:
        array (list[int]): Integer array
        start (int): Start index
        midpoint (int): Midpoint index
        end (int): End index
    """
    len_left = midpoint - start + 1
    len_right = end - midpoint

    left = [0] * len_left
    right = [0] * len_right

    for i in range(0, len_left):
        left[i] = array[start + i]

    for j in range(0, len_right):
        right[j] = array[midpoint + j + 1]

    i, j, k = 0, 0, start

    while i < len_left and j < len_right:
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < len_left:
        array[k] = left[i]
        i += 1
        k += 1

    while j < len_right:
        array[k] = right[j]
        j += 1
        k += 1


def merge_sort(array, start, end):
    """Merge Sort Algorithm

    Time complexity: O(n log n)
    Space complexity: O(n)

    Args:
        array (list[int]): Integer array
        start (int): Start index
        end (int): End index
    """
    if start >= end:
        return

    midpoint = floor((start + end) / 2)

    merge_sort(array, start, midpoint)
    merge_sort(array, midpoint + 1, end)

    merge(array, start, midpoint, end)


def main():
    """
    Main method

    """
    array = [2, 4, 6, 7, 1, 2, 3, 5]
    merge_sort(array, 0, 7)
    print(array)


if __name__ == "__main__":
    main()
