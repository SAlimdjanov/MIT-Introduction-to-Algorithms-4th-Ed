"""
heaps.py

"""

from math import floor


class Heap:
    """Heap class"""

    def __init__(self, heap):
        """Takes input array upon object initialization"""
        self.heap = heap

    def parent(self, index):
        """Returns the index of the parent node given an index of a child node"""
        return floor(index / 2)

    def left_child(self, index):
        """Returns the index of the left child of a node at a given index"""
        return 2 * index + 1

    def right_child(self, index):
        """Returns the index of the right child of a node at a given index"""
        return 2 * (index + 1)


def main():
    """
    Main method

    """
    max_heap = [16, 14, 10, 8, 7, 8, 3, 2, 4, 1]
    my_max_heap = Heap(max_heap)
    child_index = 1
    parent_index = 1

    parent_node = max_heap[my_max_heap.parent(child_index)]
    left_child_node = max_heap[my_max_heap.left_child(parent_index)]
    right_child_node = max_heap[my_max_heap.right_child(parent_index)]
    print(f"The parent of node {max_heap[child_index]} is {parent_node}")
    print(f"The left child of node {max_heap[parent_index]} is {left_child_node}")
    print(f"The right child of node {max_heap[parent_index]} is {right_child_node}")


if __name__ == "__main__":
    main()
