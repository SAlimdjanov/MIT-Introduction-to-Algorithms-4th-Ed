# Performance of Quicksort

The running time depends on how balanced each partitioning is, which depends on which elements are used as pivots. If partitions are balanced (roughly equal), the algorithm runs asymptotically as fast as merge sort. If the partitioning is unbalanced (partitions are vastly different in size), it can run asymptotically as slowly as insertion sort.

Let's briefly consider the maximum amount of memory that quicksort requires. The memory it uses (outside of the array being sorted) is not constant. Since each recursive call requires a constant amount of space on the runtime stack (outside of the array being sorted), quicksort requires space proportional to the maximum depth of recursion. That could be as bad as $\Theta (n)$ in the worst case.

### Worst-Case Partitioning

Occurs when the partitions are $0$ and $n - 1$ in size. Assume that this unbalance occurs in each recursive call. The partitioning costs $\Theta(n)$ time, which results in a total running time of $\Theta(n^2)$.

### Best-Case Partitioning

Occurs when both partitions are equal in size. In this case, `QUICKSORT` runs much faster, with a running time of $\Theta(n \lg n)$

### Average Case Partitioning

Suppose the partitioning algorithm always produced a 9-to-1 proportional split. Every level of the recursion tree has a cost $n$, until the recursion bottoms out in a base case at depth $\log_{10} n = \Theta(\lg n)$, and then the levels have a cost at most $n$. The recursion terminates at depth $\log_{10 / 9} n = \Theta(\lg n)$. Thus, with a 9-to-1 proportional split at every level of recursion, `QUICKSORT` runs in $O(n \lg n)$ time, asymptotically the same as if the split were right down the middle. Even a 99-to-1 proportionality yields the same running time. Any split of constant proportionality yields a recursion tree of depth $\Theta(\lg n)$ where the cost at each level is $O(n)$. Therefore, we can say the average case running time is $O(n \lg n)$

### Expected Running Time

From previously discussed cases, the total expected running time of `QUICKSORT` is $O(n \lg n)$.