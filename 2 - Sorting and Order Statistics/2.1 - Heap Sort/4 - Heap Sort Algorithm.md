# Heap Sort Algorithm

The algorithm given by the procedure below starts by calling the `BUILD_MAX_HEAP` procedure to build a max-heap on the input array $A[1:n]$. Since the maximum element of the array is stored at the root $A[1]$, `HEAPSORT` can place it into its correct final position by exchanging it with $A[n]$. If the procedure then discards node $n$ from the heap, (and can do it by simply decrementing `A.heap_size`) the children of the root node remain max-heaps, but the new root element might violate the max-heap property. To restore the max-heap property, the procedure just calls `MAX_HEAPIFY(A, 1)`, which leaves a max-heap in $A[1: n - 1]$. The `HEAPSORT` procedure then repeats this process for the max-heap of size $n - 1$ down to a heap of size 2.

```python
HEAPSORT(A, n)
    BUILD_MAX_HEAP(A, n)
    for i = n down to 2
        exchange A[1] with A[i]
        A.heap_size = A.heap_size - 1
        MAX_HEAPIFY(A, 1)
```

This takes $O(n \lg n)$ time, since the call to `BUILD_MAX_HEAP` takes $O(n)$ time and each of the $n - 1$ calls to `MAX_HEAPIFY` takes $O(\lg n)$ time.