"""
priority_queue.py

TODO: Implement class MinPriorityQueue

"""

from heapify import Heapify


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


def print_data(queue_obj, action):
    """Prints queue object information"""
    print()
    print({action})
    print(f"Heap: {queue_obj.heap}")
    print(f"Task List: {queue_obj.tasks}")
    print("Queue:")
    for i in queue_obj.queue:
        print(i, queue_obj.queue[i])


def main():
    """Main method"""

    max_heap = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    tasks = [
        "Task 1",
        "Task 2",
        "Task 3",
        "Task 4",
        "Task 5",
        "Task 6",
        "Task 7",
        "Task 8",
        "Task 9",
        "Task 10",
    ]

    # Implements dict to mimic mapping of tasks to indices
    queue = {max_heap[i]: tasks[i] for i in range(len(tasks))}

    max_priority_queue = MaxHeapPriorityQueue(max_heap, tasks, queue)
    print_data(max_priority_queue, "Original")

    # Max: Return max priority
    print_data(max_priority_queue, "Max")
    print(f"Maximum priority value: {max_priority_queue.maximum()}")

    # Extract max: Remove and return maximum priority
    max_priority = max_priority_queue.extract_max()
    print_data(max_priority_queue, "Extract Max")
    print(f"Highest priority ('{max_priority}') task was removed from the queue")

    # Increase Key: Change the priority of 'Professional development' to be 11
    max_priority_queue.increase_key(tasks[8], 11)
    print_data(max_priority_queue, "Increase Key")

    # Insert: Insert a new task with priority 17 into the queue
    new_task = "Urgent Matter!"
    new_priority = 17
    max_priority_queue.insert(new_task, new_priority)
    print_data(max_priority_queue, "Insert")
    print(f"Task '{new_task}' with priority {new_priority} was inserted into the queue")


if __name__ == "__main__":
    main()
