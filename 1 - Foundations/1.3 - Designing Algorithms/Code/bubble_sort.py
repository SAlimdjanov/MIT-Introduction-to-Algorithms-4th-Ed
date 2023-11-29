"""
bubble_sort.py

"""


def bubble_sort(array):
    """Bubble Sort Algorithm. Popular, but inefficent as it runs in quadratic time

    Time complexity: O(n^2)
    Space complexity: O(1)

    Args:
        array (list[int]): Input array of integers
    """
    n = len(array)

    for i in range(0, n):
        for j in range(n - 1, i, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]


def main():
    """
    Main method

    """
    array = [2, 4, 6, 7, 1, 2, 3, 5, 8, 10, 9]

    bubble_sort(array)
    print(array)


if __name__ == "__main__":
    main()
