# Sorting in Linear Time

#### A few notes before the content in this section:

At this stage, several algorithms that can sort $n$ numbers in $O(\lg n)$ time have been explored. Merge sort and heapsort achieve this upper bound in the worst case, quicksort achieves it on average. For each of these algorithms, we can produce a sequence of $n$ numbers that causes the algorithm to run in $\Omega(n \lg n)$ time.

These algorithms share an interesting property: _The sorted order they determine is based only on comparisons between the input elements_. We call such sorting algorithms **comparison sorts**. All the sorting algorithms introduced so far are comparison sorts.