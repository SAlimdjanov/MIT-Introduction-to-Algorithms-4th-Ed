"""
hiring_problem.py

"""

from random import randint


def hire_assistant(candidates, n):
    """Hire assistant procedure

    Time complexity: O(n)
    Space complexity: O(n)

    Args:
        candidates (list[int]): List of the qualification level of each candidate
        n (int): Number of candidates

    Returns:
        list[int]: Indices of list 'candidate' that were hired
    """
    best = 0
    hired_candidates = []

    for i in range(0, n):
        if candidates[i] > best:
            best = candidates[i]
            hired_candidates.append(i)

    return hired_candidates


def permute_array(array, n):
    """Permutes the array randomly in O(n^2) time in the worst case"""
    for i in range(0, n):
        array[i], array[randint(i, n - 1)] = array[randint(i, n - 1)], array[i]


def randomized_hire_assistant(candidates, n):
    """Randomized hire assistant

    Time complexity: O(n^2) worst case
    Space complexity: O(n)

    Args:
        candidates (list[int]): List of the qualification level of each candidate
        n (int): Number of candidates

    Returns:
        list[int]: Indices of list 'candidate' that were hired
    """
    permute_array(candidates, n)
    result = hire_assistant(candidates, n)
    return result


def online_hiring_problem(k, n, scores):
    """Online hiring problem implementation

    Time complexity: O(n)
    Space complexity: O(1)

    Args:
        k (int): Number of people initially interviewed
        n (int): Number of candidates
        scores (list[int]): List of candidate scores

    Returns:
        int: Index of 'scores' indicating that this is the candidate for hire
    """
    best_score = float("-inf")

    for i in range(0, k):
        if scores[i] > best_score:
            best_score = scores[i]

    for j in range(k, n):
        if scores[j] > best_score:
            return j

    return n - 1
