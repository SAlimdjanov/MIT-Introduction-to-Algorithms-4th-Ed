"""
test_queue.py

"""


from pytest import raises
from ..queue import Queue


test_queue = Queue(5)


def test_empty_queue():
    """Attempting to dequeue and empty queue throws an error"""
    with raises(ValueError):
        test_queue.dequeue()


def test_full_queue():
    """Attempting to enqueue a full queue throws an error"""
    for i in range(test_queue.size):
        test_queue.enqueue(i)

    with raises(ValueError):
        test_queue.enqueue(5)


def test_dequeue():
    """Dequeueing the first two elements behaves correctly"""
    tails, dequeued = [], []

    for _ in range(2):
        dequeued.append(test_queue.dequeue())
        tails.append(test_queue.tail)

    assert (
        dequeued == [0, 1]
        and tails == [4, 3]
        and test_queue.queue == [2, 3, 4, None, None]
    )


def test_enqueue():
    """Method enqueue moves the tail forward and correctly updates the queue"""
    test_queue.enqueue(55)

    assert test_queue.queue == [2, 3, 4, 55, None] and test_queue.tail == 4
