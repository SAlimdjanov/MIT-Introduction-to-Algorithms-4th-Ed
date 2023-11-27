"""
randomized_quicksort.py

"""

from random import randint
from quicksort import Quicksort


class RandomizedQuicksort(Quicksort):
    """Randomized Quicksort"""

    def randomized_partition(self, p, r):
        """Implements 'partition' from Quicksort with randomized pivot element"""
        i = randint(p, r)
        self.array[r], self.array[i] = self.array[i], self.array[r]
        return self.partition(p, r)

    def randomized_quicksort(self, p, r):
        """Quicksort with 'randomized_partition'"""
        if p < r:
            q = self.randomized_partition(p, r)
            self.randomized_quicksort(p, q - 1)
            self.randomized_quicksort(q + 1, r)


def main():
    """
    Main method

    """
    array = [2, 8, 7, 1, 10, 5, 6, 4, 9, 3]
    p = 0
    r = len(array) - 1

    random_sort = RandomizedQuicksort(array)
    random_sort.randomized_quicksort(p, r)

    print(random_sort.array)


if __name__ == "__main__":
    main()
