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


def main():
    """
    Main method

    """
    duplicate_array = [6, 0, 2, 0, 1, 3, 4, 6, 3, 1, 2]
    result1 = counting_sort(duplicate_array, len(duplicate_array), max(duplicate_array))
    print(result1)

    array = [0, 2, 7, 3, 4, 6, 5, 1, 8]
    result2 = counting_sort(array, len(array), max(array))
    print(result2)


if __name__ == "__main__":
    main()
