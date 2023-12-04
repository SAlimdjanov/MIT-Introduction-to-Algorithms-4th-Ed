"""
quicksort.py

"""


class Quicksort:
    """Quicksort Class"""

    def __init__(self, array):
        self.array = array

    def partition(self, p, r):
        """Partition procedure

        Time complexity: O(n)
        Space complexity: O(1)

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

    def quicksort(self, p, r):
        """Quicksort Algorithm

        Time complexity: O(n log n)
        Space complexity: O(log n) (due to the recursive call stack)

        Args:
            p (int): Start index of the array
            r (int): End index of the array
        """
        if p < r:
            q = self.partition(p, r)
            self.quicksort(p, q - 1)
            self.quicksort(q + 1, r)
