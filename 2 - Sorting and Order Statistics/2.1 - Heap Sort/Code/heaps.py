"""
heaps.py

"""

from math import floor


class Heap:
    """Heap class"""

    def __init__(self, heap):
        """
        Args:
            heap (list[int]): List representation of a valid binary heap
        """
        self.heap = heap

    def parent(self, index):
        """Returns the index of the parent node given an index of a child node. Returns 0 if called
        if arg 'index' is the root of the heap

        Args:
            index (int): Child node index

        Returns:
            int: Index of the parent node
        """
        return floor((index - 1) / 2) if index != 0 else 0

    def left_child(self, index):
        """Returns the index of the left child of a node at a given index

        Args:
            index (int): Parent node index

        Returns:
            int: Index of the left child node
        """
        return 2 * index + 1

    def right_child(self, index):
        """Returns the index of the right child of a node at a given index

        Args:
            index (int): Parent node index

        Returns:
            int: Index of the right child node
        """
        return 2 * (index + 1)
