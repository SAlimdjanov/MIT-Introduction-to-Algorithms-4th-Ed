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

The key operation in Merge Sort occurs in the combine step, which merges two adjacent, sorted subarrays. The merge operation is performed by the auxiliary procedure `MERGE(A, p, q, r)`, where the indices of the array follow $p \le q < r$. The procedure assumes that the adjacent subarrays $A[p:q]$ and $A[q+1:r]$ were already recursively sorted.

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

The procedure `MERGE_SORT(A, p, r)` sorts the elements in the subarray $A[q + 1:r]$. If $p=r$, the subarray has just one element and is therefore already sorted. Otherwise, we must have $p < r$ and `MERGE_SORT` runs the divide, conquer, and combine steps:

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

### Analysis of Divide and Conquer Algorithms

The running time of a recursive algorithm can be described with a **recurrence equation**, which describes the overall running time on a problem of size $n$ inputs in terms of the running time of the same algorithm on smaller inputs.

The recurrence for the running time of a divide and conquer algorithm is obtained through understanding the three steps. Let $T(n)$ be the worse-case running time on a problem of size $n$. If the problem is small enough, suppose $n < n_0$ for some constant $n_0 < 0$, the running time is $\Theta(1)$. Suppose the dividing step yields $a$ subproblems of size $n / b$. The running time to solve all subproblems is therefore $a T(n / b)$. Let $D(n)$ and $C(n)$ be the time to divide the subproblems and combine the solutions, respectively. The recurrence equation is therefore:

$$
T(n)=  \left\{
\begin{array}{ll}
      \Theta(1), & n < n_0 \\
      D(n) + a T(n / b) + C(n), & \text{otherwise} \\
\end{array}
\right.
$$

Sometimes, the $n / b$ size of the divide step is not an integer. For example, `MERGE_SORT` divides a problem of size $n$ into subproblems of sizes $\lceil(n / 2)\rceil$ and $\lfloor(n / 2)\rfloor$. Ignoring floors and ceilings does not generally affect the order of growth of a solution to a divide and conquer recurrence equation, so one can just say that both have size $n / 2$.

Another convention adopted here is to omit a statement of the base cases of the recurrence. This is because the base cases are pretty much always $T(n) = \Theta(1)$ if $n < n_0$ for some constant $n_0 > 0$. This is due to the running time of an algorithm on an algorithm on an input of constant size is constant.

#### Analysis of Merge Sort

Setting up the recurrence equation for the Merge Sort Algorithm:

1.  **Divide:** computes the middle of the subarray, which takes constant time. Thus, $D(n) = \Theta(1)$
2.  **Conquer:** Recursively solving two subproblems of size $n / 2$ contributes $2 T(n / 2)$ to the running time
3.  **Combine:** Since the `MERGE` procedure on an $n$-element subarray takes $\Theta(n)$ time, we have $C(n) = \Theta(n)$

When we add the functions $D(n)$ and $C(n)$ for the merge sort analysis, we are adding the function that is $\Theta(n)$ and a function that is $\Theta(1)$. This sum is a linear function of $n$. Therefore, Merge Sort's dividing and combining times together are $\Theta(n)$. Therefore, the Merge Sort recurrence is:

$$T(n) = 2 T(n / 2) + \Theta(n)$$

This recurrence relation becomes $T(n) = \Theta(n \log(n))$, which comes the the _Master Theorem_. This will be covered later.
