"""
counting_sort.py

"""


def counting_sort(array, n, k):
    """Counting sort algorithm

    Time complexity: O(n + k)
    Space complexity: O(n + k)

    Args:
        array (list[int]): Input array
        n (int): Number of elements in the input array
        k (int): Maximum value of the input array

    Returns:
        list[int]: Sorted array
    """
    sorted_output = [0] * n
    memo = [0] * (k + 1)

    for j in range(n):
        memo[array[j]] = memo[array[j]] + 1

    for i in range(1, k + 1):
        memo[i] = memo[i] + memo[i - 1]

    for x in range(n - 1, -1, -1):
        sorted_output[memo[array[x]] - 1] = array[x]
        memo[array[x]] = memo[array[x]] - 1

    return sorted_output
