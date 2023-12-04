# Minimum and Maximum

How many comparisons are required to determine the minimum of a set of $n$ elements? To obtain an upper bound of $n - 1$ comparisons, just examine each element of the set in turn and keep track of the smallest element seen so far. The `MINIMUM` procedure assumes that the set resides in the array $A[1: n]$:

```python
MINIMUM(A, n)
    min = A[1]
    for i = 2 to n
        if min > A[i]
            min = A[i]
    return min
```

The same method is used for `MAXIMUM`. This is the best algorithm because there's a lower bound of $n - 1$ comparisons for the problem of determining the minimum/maximum. Hence, this algorithm is optimal.

### Simultaneous Minimum and Maximum

Some applications require this. For example, a graphics program may need to scale a set of $(x, y)$ data to fit onto a display screen. To do so, the program must first determine the minimum and maximum value of each coordinate.

Of course, we can determine both the minimum and maximum of $n$ elements using $\Theta(n)$ comparisons. We simply find the values independently, using $n - 1$ comparisons for each, for a total of $2n - 2 = \Theta(n)$ comparisons. Although this is asymptotically optimal, it is possible to improve the leading constant. We can find the values using at most $3 \lfloor n / 2 \rfloor$ comparisons. The trick is to maintain both the minimum and maximum elements seen thus far. Rather than proccessing each element of the input by comparing it against the current minimum and maximum, at a cost of 2 comparisons, process elements in pairs. Compare pairs of elements from the input first with each other, and then compare the smaller with the current minimum and the larger to the current maximum, at a cost of 3 comparisons for every two elements.