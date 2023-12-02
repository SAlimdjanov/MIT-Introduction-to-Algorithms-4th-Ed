"""
test_priority_queue.py

"""

from copy import deepcopy
from ..priority_queue import MaxHeapPriorityQueue


### Test Data ###

heap = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
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
queue = {heap[i]: tasks[i] for i in range(len(tasks))}

# Priority Queue Object
priority_queue = MaxHeapPriorityQueue(heap, tasks, queue)


def test_max():
    """Test 'max' operation on the queue above"""
    assert priority_queue.maximum() == 16


def test_extract_max():
    """Test 'extract-max' operation on the queue above"""
    expected_heap = deepcopy(heap)
    del expected_heap[0]

    expected_tasks = deepcopy(tasks)
    del expected_tasks[0]

    expected_queue = deepcopy(queue)
    del expected_queue[priority_queue.maximum()]

    assert (
        priority_queue.extract_max() == 16
        and priority_queue.heap == expected_heap
        and priority_queue.tasks == expected_tasks
        and priority_queue.queue == expected_queue
    )


def test_increase_key():
    """Test 'increase-key' operation on the queue above"""
    expected_heap = [14, 11, 8, 10, 9, 3, 2, 4, 7]
    expected_tasks = [
        "Task 2",
        "Task 10",
        "Task 4",
        "Task 3",
        "Task 6",
        "Task 7",
        "Task 8",
        "Task 9",
        "Task 5",
    ]
    expected_queue = {
        expected_heap[i]: expected_tasks[i] for i in range(len(expected_heap))
    }

    priority_queue.increase_key(tasks[8], 11)

    assert (
        priority_queue.heap == expected_heap
        and priority_queue.tasks == expected_tasks
        and priority_queue.queue == expected_queue
    )


def test_insert():
    """Test 'insert' operation on the queue above"""
    expected_heap = [17, 14, 8, 10, 11, 3, 2, 4, 7, 9]
    expected_tasks = [
        "Urgent Matter!",
        "Task 2",
        "Task 4",
        "Task 3",
        "Task 10",
        "Task 7",
        "Task 8",
        "Task 9",
        "Task 5",
        "Task 6",
    ]
    expected_queue = {
        expected_heap[i]: expected_tasks[i] for i in range(len(expected_heap))
    }

    priority_queue.insert("Urgent Matter!", 17)

    assert (
        priority_queue.heap == expected_heap
        and priority_queue.tasks == expected_tasks
        and priority_queue.queue == expected_queue
    )
