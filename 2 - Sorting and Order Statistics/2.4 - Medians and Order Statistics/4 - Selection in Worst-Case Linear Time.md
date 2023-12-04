# Selection in Worst-Case Linear Time

Here, a remarkable and theoretically interesting selection algorithm whose running time is $\Theta(n)$ in the worst-case is examined. The previous algorithm has a quadratic worse-case running time. However, this algorithm is not as practical as the previous.

The `SELECT` algorithm below guarantees a good split by choosing a provably good pivot when partitioning the array. The cleverness here, is that it finds the pivot recursively. Thus, there are two invokations of select: one to find a good pivot, and a second to recursively find the desired order statistic.

The partitioning algorithm used by select is like the deterministic partitioning algorithm `PARTITION` from quicksort, but modified to take the element to partition around as an additional parameter. Like `PARTITION`, the `PARTITION_AROUND` algorithm returns the index of the pivot. Since it is so similar to `PARTITION`, the pseudocode of `PARTITION_AROUND` is omitted.

The `SELECT` procedure takes as input a subarray $A[p: r]$ of $n = r - p + 1$ elements and an integer $i$ in the range $1 \le i \le n$. It returns the $i$-th smallest element of $A$:

```python
SELECT(A, p, r, i)
    while (r - p + 1) mod 5 != 0
        for j = p + 1 to r  # Put the minimum into A[p]
            if A[p] > A[j]
                swap A[p] with A[j]
        # If we want the minimum of A[p: r], we're done
        if i == 1
            return A[p]
        # Otherwise, we want the (i - 1)st element of A[p + 1: r]
        p = p + 1
        i = i - 1
    g = (r - p + 1) / 5  # Number of 5-element groups
    for j = p to p + g - 1  # Sort each group
        sort <A[j], A[j + g], A[j + 2 * g], A[j + 3 * g], A[j + 4 * g]> in place
    # All group medians now lie in the middle fifth of A[p: r]
    # Find the pivot x recursively as the median of the group medians
    x = SELECT(A, p + 2 * g, p + 3 * g - 1, ceil(g / 2))
    q = PARTITION_AROUND(A, p, r, x)  # Partition around the pivot
    # The rest is just like lines 3-9 of RANDOMIZED_SELECT
    k = q - p + 1
    if i == k
        return A[q]  # Pivot is the answer
    elif i < k
        return SELECT(A, p, q - 1, i)
    else
        return SELECT(A, q + 1, r, i - k)
```

## Analysis

The judicious choice of the pivot `x` plays into a guarantee of the worst-case running time. The following theorem consolidates the analysis:

_**Theorem:** The running time of_ `SELECT` _on an input of_ $n$ _elements is_ $\Theta(n)$.