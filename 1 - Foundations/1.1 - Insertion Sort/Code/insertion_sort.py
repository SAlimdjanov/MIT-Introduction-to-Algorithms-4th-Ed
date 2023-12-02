"""
insertion_sort.py

"""


def insertion_sort(sequence, n):
    """Insertion Sort Algorithm

    Time complexity: O(n^2)
    Space complexity: O(n)

    Args:
        sequence (list[int]): Sequence of integers
        n (int): Number of elements

    Returns:
        list[int]: Sorted sequence
    """
    for i in range(1, n):
        key = sequence[i]
        j = i - 1

        while j >= 0 and sequence[j] > key:
            sequence[j + 1] = sequence[j]
            j -= 1

        sequence[j + 1] = key

    return sequence


def insertion_sort_reversed(sequence, n):
    """Reversed Insertion Sort Algorithm

    Time complexity: O(n^2)
    Space complexity: O(n)

    Args:
        sequence (list[int]): Sequence of integers
        n (int): Number of elements

    Returns:
        list[int]: Sorted sequence (descending order)
    """
    for i in range(1, n):
        key = sequence[i]
        j = i - 1

        while j >= 0 and sequence[j] < key:
            sequence[j + 1] = sequence[j]
            j -= 1

        sequence[j + 1] = key

    return sequence


def binary_array_addition(bin_a, bin_b, n):
    """
    Performs binary addition of two n bit binary numbers stored in lists.

    Time complexity: O(n)
    Space complexity: O(n)

    Args:
        bin_a (list[int]): List of integers valued 0 or 1
        bin_b (list[int]): List of integers valued 0 or 1
        n (_type_): Length of A and B

    Returns:
        list[int]: The resulting list C
    """
    bin_c = [0] * (n + 1)
    carry_bit = 0

    for i in range(n - 1, -1, -1):
        total = bin_a[i] + bin_b[i] + carry_bit
        bin_c[i + 1] = total % 2
        carry_bit = total // 2

    bin_c[0] = carry_bit

    return bin_c
