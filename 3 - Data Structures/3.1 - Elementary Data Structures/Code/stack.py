"""
stacks.py

Implements stacks in constant time and space complexity

"""


class Stack:
    """Implements stack operations on an array"""

    def __init__(self, size):
        """Initializes empty stack of a specific size

        Args:
            size (int): Maximum size of the stack
        """
        self.size = size
        self.stack = [None] * size
        self.top = 0

    def stack_empty(self):
        """Checks if the stack is empty

        Returns:
            bool: Is the stack empty?
        """
        return self.top == 0

    def push(self, x):
        """Pushes an element into the stack

        Args:
            x (int): Value to be placed in the stack
        """
        if self.top == self.size:
            raise ValueError("Stack overflow")

        self.top += 1
        self.stack[self.top - 1] = x

    def pop(self):
        """Removes an element from the stack

        Returns:
            int: Removed element
        """
        if self.stack_empty():
            raise ValueError("Stack underflow")

        self.top -= 1
        value = self.stack[self.top]
        self.stack[self.top] = None

        return value
