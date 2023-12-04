# Selection in Expected Linear Time

The general selection problem appears more difficult than the simple problem of finding a maximum. Surprisingly, the asymptotic running time is the same for both: $\Theta(n)$. This section presents a divide-and-conquer algorithm for the selection problem. The `RANDOMIZED_SELECT` procedure is modelled after the quicksort algorithm. However, unlike quicksort, the procedure only works on one side of the partition. Therefore, the running time is $\Theta(n)$ instead of quicksort's $\Theta(n \lg n)$ running time.

The `RANDOMIZED_SELECT` procedure returns the $i$-th smallest element of the array $A[p: r]$, where $1 \le i \le r - p + 1$:

```python
RANDOMIZED_SELECT(A, p, r, i)
    if p == r
        # Base case: When p == r, i = 1
        return A[p]
    q = RANDOMIZED_PARTITION(A, p, r)
    k = q - p + 1
    if i == k
        return A[q]  # Pivot element is the answer
    elif i < k
        return RANDOMIZED_SELECT(A, p, q - 1, i)
    else
        return RANDOMIZED_SELECT(A, q + 1, r, i - k)
```

## Analysis

The worst-case running time of this algorithm is $\Theta(n^2)$, even to find the minimum, because it could be extremely unlucky and always partition around the largest remaining element before identifying the $i$-th smallest when only one element remains. In the worst case, each recursive step removes only the pivot from consideration. Because partitioning $n$ elements takes $\Theta(n)$ time, the the recurrence for this algorithm is the same as quicksort, and yields the same solution $T(n) = \Theta(n^2)$. Because the algorithm is randomized, no particular input elicits the worse-case behavior, allowing us to conclude that it has an expected linear running time, as seen below:

_**Lemma:** A partitioning is helpful with probability at least_ $1 / 2$.

_**Theorem:** The procedure_ `RANDOMIZED_SELECT` _on an input array of_ $n$ _elements has an expected running time of_ $\Theta(n)$.

This leads to a more general conclusion that the expected running time of $O(n)$.