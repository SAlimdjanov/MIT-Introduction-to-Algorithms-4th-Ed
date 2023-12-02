"""
priority_queue.py

TODO: Implement class MinPriorityQueue

"""

from .heapify import Heapify


class MaxHeapPriorityQueue(Heapify):
    """Priority Queue Class"""

    def __init__(self, heap, tasks, queue):
        super().__init__(heap)
        self.tasks = tasks
        self.queue = queue

    def maximum(self):
        """Returns the max value of the max-heap

        Time complexity: O(1) (since we always return the first element for max-heaps)
        Space complexity: O(1)

        Raises:
            ValueError: If there are no elements in the heap

        Returns:
            int: Max priority value
        """
        if self.heap_size < 1:
            raise ValueError("Heap underflow")

        return self.heap[0]

    def extract_max(self):
        """Removes and returns the max value of the max-heap. With a max-heap, this will always be
        the element at index 0

        Time complexity: O(log n)
        Space complexity: O(n)

        Returns:
            int: Max priority value
        """
        max_elem = self.maximum()

        # Delete priority, and the task associated with it
        del self.heap[0]
        del self.tasks[0]
        del self.queue[max_elem]

        # Update heap size and fix the heap
        self.heap_size -= 1
        self.max_heapify(0)

        return max_elem

    def increase_key(self, selected_task, k):
        """Increase key operation

        Args:
            selected_task (str): Task subjected to a priority (key) change
            k (int): New key for 'selected task'

        Time complexity: O(log n)
        Space complexity: O(n)

        Raises:
            ValueError: When 'k' is smaller than the original key
        """
        old_key = next(
            (key for key, value in self.queue.items() if value == selected_task)
        )

        # Validate new key
        if k < old_key:
            raise ValueError("New key is smaller than current key")

        # Update 'queue' and 'heap' with the new priority
        self.queue = {
            k if key == old_key else key: value for key, value in self.queue.items()
        }
        self.heap[self.heap.index(old_key)] = k

        # Fix the new heap to be max-heap compliant, update queue accordingly
        i = self.heap.index(k)

        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = (
                self.heap[self.parent(i)],
                self.heap[i],
            )

            self.tasks[i], self.tasks[self.parent(i)] = (
                self.tasks[self.parent(i)],
                self.tasks[i],
            )

            i = self.parent(i)

        # Re-construct queue with new priorities
        self.queue = {self.heap[i]: self.tasks[i] for i in range(self.heap_size)}

    def insert(self, task, priority):
        """Insert a task into the priority queue

        Time complexity: O(log n)
        Space complexity: O(1)

        Args:
            task (str): Name of task to be inserted
            priority (int): Priority value

        """
        self.heap_size += 1
        k = priority
        priority = float("-inf")
        self.heap.append(priority)
        self.tasks.append(task)
        self.queue[priority] = task
        self.increase_key(self.tasks[-1], k)
