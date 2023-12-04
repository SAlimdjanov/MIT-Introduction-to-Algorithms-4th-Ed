# Introduction

The $i$-th **order statistic** of a set of $n$ elements is the $i$-th smallest element. For example, the **minimum** of a set of elements is the order statistic $i = 1$ and the **maximum** is the $n$-th order statistic, $i = n$. Informally, a **median** is the "halfway" point of the set. When $n$ is odd, the median is unique, occuring at $i = (n + 1) / 2$. When $n$ is even, there are two medians, the **lower median** occuring at $i = n / 2$ and the **higher median** occuring and $i = n / 2 + 1$. Thus, regardless of the parity of $n$, the medians occur at $i = \lfloor (n + 1) / 2 \rfloor$ and $i = \lceil (n + 1) / 2 \rceil$. For now, "the median" refers to the lower median.

The problem presented in this section is selecting the $i$-th order statistic from a set of $n$ distinct numbers. Assume for convenience that the set contains distinct numbers, although virtually everything that we do extends to the situation in which a set contains repeated values.

We formally define the **selection problem** as follows:

-   **Input:** A set $A$ of $n$ distinct numbers and an integer $i$, with $1 \le i \le n$
-   **Output:** The element $x \in A$ that is larger than exactly $i - 1$ elements of $A$

We can solve the selection problem in $O(n \lg n)$ time simply by sorting the numbers using heapsort or merge sort and then outputting the $i$-th element in the sorted array. This section presents asymptotically faster algorithms.