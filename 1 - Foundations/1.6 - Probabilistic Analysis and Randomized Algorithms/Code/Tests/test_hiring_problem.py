"""
test_hiring_problem.py

"""

from ..hiring_problem import hire_assistant, online_hiring_problem


def test_hire_assistant():
    """Ensure function hire_assistant hires the correct candidates"""
    # This validates randomizedHireAssistant too, because only a permuted array is inputted to the
    # same method, hireAssistant
    candidates = [3, 2, 6, 4, 5, 1]
    expected_result = [0, 2]

    result = hire_assistant(candidates, len(candidates))

    assert result == expected_result


def test_online_hiring_problem():
    """Ensures the correct candidates are being hired by function online_hiring_problem"""
    k = 3
    scores = [4, 7, 2, 10, 2, 6]

    result = online_hiring_problem(k, len(scores), scores)
    expected_result = scores.index(10)

    assert result == expected_result
