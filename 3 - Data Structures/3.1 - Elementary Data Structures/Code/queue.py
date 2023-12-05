"""
queue.py

"""


class Queue:
    """Implements the (non-circular) queue data structure

    Time complexity: O(1)
    Space complexity: O(n)

    """

    def __init__(self, size):
        """Initializes empty queue of a specific size

        Args:
            size (int): Maximum size of the queue
        """
        self.size = size
        self.queue = [None] * self.size
        self.tail = 0
        self.head = 0

    def enqueue(self, x):
        """Adds an element to the queue

        Args:
            x (int): Element to be added
        """
        if self.tail == self.size:
            raise ValueError("Queue is full")

        self.queue[self.tail] = x
        self.tail += 1

    def dequeue(self):
        """Removes the element first-in-line in the queue

        Returns:
            int: Value removed from the queue
        """
        if self.head == self.tail:
            raise ValueError("Queue is empty")

        x = self.queue[self.head]
        self.queue[self.head] = None

        if self.tail == self.size:
            self.head = 0

        # Delete spot used by removed element and append new spot to the back
        del self.queue[0]
        self.queue.append(None)

        # Shift tail back to allow another element to be enqueued
        self.tail -= 1

        return x


# my_queue = Queue(5)

# for i in range(my_queue.size):
#     my_queue.enqueue(i)

# print(my_queue.queue)

# print("dequeued", my_queue.dequeue())
# print(my_queue.queue)

# my_queue.enqueue(11)
# print(my_queue.queue)

# print("dequeued", my_queue.dequeue())
# print(my_queue.queue)

# my_queue.enqueue(12)
# print(my_queue.queue)

# my_queue.enqueue(12)
# print(my_queue.queue)
