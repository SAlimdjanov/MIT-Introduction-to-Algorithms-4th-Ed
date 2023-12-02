"""
test_heaps.py

"""


from ..heaps import Heap


# Max Heap
max_heap = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
heap_nodes = Heap(max_heap)
HEAP_LEN = len(max_heap)

# Expected values (Compliant Max Heap)
exp_parents = [0, 0, 0, 1, 1, 2, 2, 3, 3, 4]
exp_left_children = [(2 * i + 1) for i in range(HEAP_LEN)]
exp_right_children = [(2 * i + 2) for i in range(HEAP_LEN)]


def generate_results(funct):
    """Iteratively generates results lists for several unit tests below

    Args:
        funct (method): Function

    Returns:
        list: Results of calling 'funct' HEAP_LEN times through the heap
    """
    results = []
    for i in range(HEAP_LEN):
        results.append(funct(i))

    return results


def test_parent():
    """parent method returns correct parent nodes"""
    results = generate_results(heap_nodes.parent)
    assert results == exp_parents


def test_left_children():
    """left_child methods return correct left child nodes"""
    results = generate_results(heap_nodes.left_child)
    assert results == exp_left_children


def test_right_children():
    """left_child methods return correct left child nodes"""
    results = generate_results(heap_nodes.right_child)
    assert results == exp_right_children
