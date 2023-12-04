"""
randomized_select.py

"""

from random import randint


class RandomizedSelect:
    """Implements Randomized Select Algorithm"""

    def __init__(self, array):
        self.array = array

    def partition(self, p, r):
        """Partition procedure (From Quicksort)

        Time complexity: O(n)
        Space complexity: O(1)

        Args:
            p (int): Start index
            r (int): End index

        Returns:
            int: Pivot element index
        """
        x = self.array[r]
        i = p - 1

        for j in range(p, r):
            if self.array[j] <= x:
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]

        self.array[i + 1], self.array[r] = self.array[r], self.array[i + 1]

        return i + 1

    def randomized_partition(self, p, r):
        """Generates a partition on the randomized inputarray"""
        i = randint(p, r)
        self.array[r], self.array[i] = self.array[i], self.array[r]

        return self.partition(p, r)

    def randomized_select(self, p, r, i):
        """Randomized Select Algorithm

        Time complexity: O(n)
        Space complexity: O(log n) - Recursion depth

        Args:
            p (int): Start index
            r (int): End index
            i (int): Desired i-th order statistic

        Returns:
            int: Value of the i-th order statistic
        """
        if p == r:
            return self.array[p]

        q = self.randomized_partition(p, r)
        k = q - p + 1

        if i == k:
            return self.array[q]

        if i < k:
            return self.randomized_select(p, q - 1, i)

        return self.randomized_select(q + 1, r, i - k)
