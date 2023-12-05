"""
test_stacks.py

"""


from pytest import raises
from ..stack import Stack


# Initialize a 4-element stack for the tests
test_stack = Stack(4)


def test_underflow():
    """Exception is raised when pop is attempted on an empty stack"""
    with raises(IndexError):
        test_stack.pop()


def test_stack_empty():
    """Empty stack is detected"""
    assert test_stack.stack_empty()


def test_push():
    """Stack responds correctly to several pushes"""
    test_stack.push(55)
    test_stack.push(23)
    test_stack.push(11)

    assert test_stack.stack == [55, 23, 11, None] and test_stack.top == 3


def test_stack_not_empty():
    """After operations, stack should not be empty"""
    assert not test_stack.stack_empty()


def test_overflow():
    """Stack overflow occurs when 2 elements are pushed"""
    test_stack.push(27)

    with raises(IndexError):
        test_stack.push(64)


def test_pop():
    """Ensures all correct elements are popped and the 'top' values are correct. Also checks if the
    stack is fully empty"""
    popped, tops = [], []

    for _ in range(test_stack.size):
        popped.append(test_stack.pop())
        tops.append(test_stack.top)

    assert (
        tops == [3, 2, 1, 0]
        and popped == [27, 11, 23, 55]
        and test_stack.stack_empty()
        and test_stack.stack == [None, None, None, None]
    )
