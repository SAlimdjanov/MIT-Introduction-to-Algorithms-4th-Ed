"""
bucket_sort.py

"""


def bucket_sort(array, n):
    """Bucket sort algorithm

    Time complexity: O(n + k) (k is the number of buckets created)
    Space complexity: O(n + k)

    Args:
        array (list[float]): List of values between 0 and 1
        n (int): Length of 'array'

    Returns:
        list[float]: Sorted array
    """
    aux_array = [[] for _ in range(n)]

    for i in range(n):
        index = int(n * array[i])
        aux_array[index].append(array[i])

    for i in range(n):
        aux_array[i].sort()

    sorted_array = []

    for i in range(n):
        sorted_array.extend(aux_array[i])

    return sorted_array
