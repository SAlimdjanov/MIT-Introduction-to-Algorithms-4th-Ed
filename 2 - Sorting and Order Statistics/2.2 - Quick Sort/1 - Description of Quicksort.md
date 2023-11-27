# Description of Quicksort

Like 'Merge Sort', it applies the divide-and-conquer method previously introduced. Here's the process:

1.  **Divide:** Partition the array $A[p: r]$ into two (possibly empty) subarrays, **high side** ($A[q + 1:r]$) and **low side** ($A[p:q - 1]$) such that each element in the low side of the partition is less than or equal to the **pivot** element $A[q]$, which is less than or equal to each element in the high side. Compute the index $q$ of the pivot as part of this partitioning procedure.
2.  **Conquer:** Call `QUICKSORT` recursively to sort both of the subarrays.
3.  **Combine:** Do nothing. The subarrays are already sorted by this point!

To sort an entire $n$-element array $A[1: n]$, the initial call is `QUICKSORT(A, 1, n)`.

```python
QUICKSORT(A, p, r)
    if p < r
        q = PARTITION(A, p, r)  # Partition around pivot
        QUICKSORT(A, p, q - 1)  # Sort low side
        QUICKSORT(A, q + 1, r)  # Sort high side
```

## Partitioning the Array

```python
PARTITION(A, p, r)
    x = A[r]   # Pivot element
    i = p - 1  # Highest index into low side
    for j = p to r - 1               # Process each element other than the pivot
        if A[j] <= x                 # Does this element belong on the low side?
            i = i + 1                # Index of a new slot on the low side
            exchange A[i] with A[j]  # Put this element here
    exchange A[i + 1] with A[r]      # Pivot goes just to the right of the low side
    return i + 1                     # New index of the pivot
```

`PARTITION` always selects the element $x = A[r]$ as the pivot. As the procedure runs, each element falls exactly into one of four regions, some of which may be empty. At the start of each iteration of the `for` loop, the regions satisfy certain properties, stated in this loop invariant:

At the beginning of each iteration of the loop, for any array index $k$, the following conditions hold:

1.  if $p \le k \le i$, then $A[k] \le x$
2.  if $i + 1 \le k \le j - 1$, then $A[k] > x$
3.  if $k = r$, then $A[k] = x$

The output of `PARTITION` now satisfies the specifications given in the **divide** step. In fact, it satisfies a slightly stronger condition: After line 3 of `QUICKSORT`, $A[q]$ is strictly less than every element of $A[q + 1: r]$.

## Randomized Quicksort

Randomizing the pivot element increases the chances of the subarray balancing being more balanced. The changes to the original procedures are below:

```python
RANDOMIZED_PARTITION(A, p, r)
    i = RANDOM(p, r)
    exchange A[r] with A[i]
    return PARTITION(A, p, r)
```

```python
RANDOMIZED_QUICKSORT(A, p, r)
    if p < r
        q = RANDOMIZED_PARTITION(A, p, r)
        RANDOMIZED_QUICKSORT(A, p, q - 1)
        RANDOMIZED_QUICKSORT(A, q + 1, r)
```