# The Divide and Conquer Method

Many useful algorithms are recursive and typically follow the **Divide and Conquer** method:

1.  **Divide** the problem into one or more subproblems that are smaller instances of the same problem
2.  **Conquer** the subproblems by solving them recursively
3.  **Combine** the subproblem solutions to form a solution to the original problem

## Merge Sort Algorithm

This algorithm follows the Divide and Conquer method; it sorts a subarray $A[p:r]$, starting with the entire array $A[1:n]$ and recursing down to smaller and smaller subarrays:

1.  **Divide** the subarray $A[p:r]$ to be sorted into two adjacent arrays, each of half the size. To do so, compute the midpoint $q$ of $A[p:r]$ (taking the average of $p$ and $r$), and divide $A[p:r]$ into subarrays $A[p:q]$ and $A[q+1:r]$
2.  **Conquer** by sorting the two sorted subarrays $A[p:q]$ and $A[q+1:r]$ recursively using merge sort
3.  **Combine** by merging the two sorted subarrays $A[p:q]$ and $A[q+1:r]$, producing the sorted answer

The recursion "caps out" when it reaches the base case: $\text{length}\left(A[p:r]\right)=1$, when $p=r$. As noted in `INSERTION_SORT`'s loop invariant, a subarray comprising of a single element is always sorted.

The key operation in Merge Sort occurs in the combine step, which merges two adjacent, sorted subarrays. The merge operation is performed by the auxiliary procedure `MERGE(A, p, q, r)`, where the indices of the array follow $p<=q<r$. The procedure assumes that the adjacent subarrays $A[p:q]$ and $A[q+1:r]$ were already recursively sorted.

Each basic step of the sort takes constant time and the total number of basic steps being between $n/2$ and $n$, we can say that merging takes $\Theta(n)$ time. The Merge procedure pseudocode is below:

```python
MERGE(A, p, q, r)
    # length of A[p:q]
    nL = q - p + 1

    # length of A[q + 1:r]
    nR = r - q

    # Create subarrays
    let L[0: nL - 1] and R[0: nR - 1] be new arrays

    # Copy A[p:q] into L[0: nL - 1]
    for i = 0 to nL - 1
        L[i] = A[p + i]

    # Copy A[q + 1:r] into R[0: nR - 1]
    for j = 0 to nR - 1
        R[j] = A[q + j + 1]

    i = 0  # i indexes the smallest remaining element in L
    j = 0  # j indexes the smallest remaining element in R
    k = p  # k indexes the location in A to fill

    # As long as each of the arrays L and R contain an unmerged
    # element, copy the smallest unmerged element back into
    # A[p:r]
    while i < nL and j < nR
        if L[i] <= R[j]
            A[k] = L[i]
            i = i + 1
        else A[k] = R[j]
            j = j + 1
        k = k + 1

    # Having gone through one of L or R entirely, copy the
    # remainder of the other to the end of A[p:r]
    while i < nL
        A[k] = L[i]
        i = i + 1
        k = k + 1
    while j < nR
        A[k] = R[j]
        j = j + 1
        k = k + 1
```

The procedure `MERGE_SORT(A, p, r)` sorts the elements in the subarray $A[q + 1:r]$. If $p=r$, the subarray has just one element and is therefore already sorted. Otherwise, we must have $p<r$ and `MERGE_SORT` runs the divide, conquer, and combine steps:

```python
MERGE_SORT(A, p, r)
    # Zero or one element?
    if p >= r
        return

    # Compute midpoint of A[p:r]
    q = floor((p + r) / 2)

    # Recursively sort both subarrays
    MERGE_SORT(A, p, q)
    MERGE_SORT(A, q + 1, r)

    # Merge the subarrays
    MERGE(A, p, q, r)
```
