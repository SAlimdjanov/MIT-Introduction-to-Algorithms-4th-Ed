# Maintaining the Heap Property

The procedure below maintains the max-heap property. Its inputs are an array $A$ with the _heap-size_ attribute and an index $i$ into the array. When it is called, `MAX_HEAPIFY` assumes that the binary trees rooted at `LEFT(i)` and `RIGHT(i)` are max-heaps, but $A[i]$ might be smaller than its children, this violating the max-heap property. `MAX_HEAPIFY` lets the value at $A[i]$ float down in the max-heap so that the subtree rooted at index $i$ obeys the max-heap property.

## `MAX_HEAPIFY` Procedure

```python
MAX_HEAPIFY(A, i)
    l = LEFT(i)
    r = RIGHT(i)
    if l <= A.heap_size and A[l] > A[i]
        largest = l
    else
        largest = i
    if r <= A.heap_size and A[r] > A[largest]
        largest = r
    if largest != i
        swap A[i] with A[largest]
        MAX_HEAPIFY(A, largest)
```

## Explanation and Analysis of `MAX_HEAPIFY`

Each step determines the largest of the elements, `A[i]`, `A[LEFT(i)]`, and `A[RIGHT(i)]` and stores the index of the largest element in `largest`. If `A[i]` is largest, then the subtree rooted at node $i$ is already a max-heap and nothing else needs to be done. Otherwise, one of the two children contains the largest element. Positions `i` and `largest` swap their contents, which causes node `i` and its children to satisfy the max-heap property.

Suppose $T(n)$ is the worst-case running time that the procedure takes on a subtree of size at most $n$. For a tree rooted at a given node $i$, the running time is the $\Theta(1)$ time to fix up the relationships among the elements `A[i]`, `A[LEFT(i)]`, and `A[RIGHT(i)]`, plus the time to run `MAX_HEAPIFY` on a subtree rooted at one of the children of node $i$ (Assuming the recursive call occurs). The children's subtrees each have size at most $2 n / 3$, and therefore we can descrive the running time of the procedure by the following recurrence inequality:

$$T(n) \le T \left(\frac{2 n}{3}\right) + \Theta(1)$$

This evaluates to a running time of $T(n) = O(\lg n)$. Alternatively, the running time of `MAX_HEAPIFY` on a node of height $h$ is $O(h)$.
