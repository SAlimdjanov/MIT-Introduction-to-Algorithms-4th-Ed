"""
min_and_max.py

Algorithmic complexities for both methods are:

Time complexity: O(n)
Space complexity: O(1)

TODO: Implement simultaneuous_min_max()

"""


class MinAndMax:
    """Class Min and Max"""

    def __init__(self, array):
        self.array = array
        self.n = len(array)

    def minimum(self):
        """Minimum procedure

        Returns:
            int: Maximum value of the input array
        """
        min_val = self.array[0]

        for i in range(1, self.n):
            if min_val > self.array[i]:
                min_val = self.array[i]

        return min_val

    def maximum(self):
        """Maximum procedure

        Returns:
            int: Maximum value of the input array
        """
        max_val = self.array[0]

        for i in range(1, self.n):
            if max_val < self.array[i]:
                max_val = self.array[i]

        return max_val
