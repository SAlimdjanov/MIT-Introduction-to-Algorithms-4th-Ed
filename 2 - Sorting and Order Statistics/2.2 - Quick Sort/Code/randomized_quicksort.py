"""
randomized_quicksort.py

"""

from random import randint
from .quicksort import Quicksort


class RandomizedQuicksort(Quicksort):
    """Randomized Quicksort"""

    def randomized_partition(self, p, r):
        """Implements 'partition' from Quicksort with randomized pivot element"""
        i = randint(p, r)
        self.array[r], self.array[i] = self.array[i], self.array[r]
        return self.partition(p, r)

    def randomized_quicksort(self, p, r):
        """Quicksort with the 'randomized_partition' method"""
        if p < r:
            q = self.randomized_partition(p, r)
            self.randomized_quicksort(p, q - 1)
            self.randomized_quicksort(q + 1, r)
