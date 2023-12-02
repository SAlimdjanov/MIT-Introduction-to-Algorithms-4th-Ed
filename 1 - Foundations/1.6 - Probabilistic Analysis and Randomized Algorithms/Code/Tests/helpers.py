"""
helpers.py

"""

from random import randint


def permute_array(array, n):
    """Permute and input array"""
    for i in range(0, n):
        array[i], array[randint(i, n - 1)] = array[randint(i, n - 1)], array[i]
