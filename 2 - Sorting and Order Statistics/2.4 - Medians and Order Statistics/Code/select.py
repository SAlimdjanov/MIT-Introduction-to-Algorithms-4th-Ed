"""
select.py

"""


from math import floor, ceil


class Select:
    """Implements Select Algorithm"""

    def __init__(self, array):
        self.array = array

    def partiton_around(self, p, r, x):
        """Modified partition method, the same as the one used in 'randomized_select', only the
        pivot element is passed in as an argument.

        Returns:
            int: New pivot element index
        """
        i = p - 1

        for j in range(p, r + 1):
            if self.array[j] <= x:
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]

        self.array[i + 1], self.array[r] = self.array[r], self.array[i + 1]

        return i + 1

    def select(self, p, r, i):
        """A modified version of 'randomized_select' with the same arguments

        Time complexity: O(n)
        Space complexity: O(log n) - recursion depth

        Returns:
            int: Value of the i-th order statistic
        """
        while (r - p + 1) % 5 != 0:
            for j in range(p + 1, r + 1):
                if self.array[p] > self.array[j]:
                    self.array[p], self.array[j] = self.array[j], self.array[p]

            if i == 1:
                return self.array[p]

            p += 1
            i -= 1

        g = floor((r - p + 1) / 5)

        for j in range(p, p + g - 1):
            indices = [j, j + g, j + 2 * g, j + 3 * g, j + 4 * g]
            elements = [self.array[index] for index in indices]
            elements.sort()

            for index, sorted_value in zip(indices, elements):
                self.array[index] = sorted_value

        x = self.select(p + 2 * g, p + 3 + g - 1, ceil(g / 2))
        q = self.partiton_around(p, r, x)

        k = q - p + 1

        if i == k:
            return self.array[q]

        if i < k:
            return self.select(p, q - 1, i)

        return self.select(q + 1, r, i - k)
