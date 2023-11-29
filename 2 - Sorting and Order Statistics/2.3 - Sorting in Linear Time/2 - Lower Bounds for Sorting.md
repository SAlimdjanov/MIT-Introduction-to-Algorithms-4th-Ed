# Lower Bounds for Sorting

A comparison sort uses only comparisons between elements to gain order information about an input sequence $\left< a_1, a_2, ..., a_n \right>$. Given two elements $a_i$ and $a_j$, it performs one of the tests:

$$
\begin{align*}
a_i &< a_j, &(1) \\
a_i &\le a_j, &(2) \\
a_i &= a_j, &(3)\\
a_i &\ge a_j, &(4)\\
a_i &> a_j &(5)\\
\end{align*}
$$

This is to determine their relative order. It may not inspect the values of the elements or gain order information about them in any other way.

Since we are proving a lower bound, we assume without loss of generality in this section that all the input elements are distinct. A lower bound for distinct elements applies when elements may or may not be distinct. Consequently, comparisons of the form in test $(3)$ are useless, which means we can assume that no comparisons for exact equality occur. Moreover, the rest of the comparison tests are all equivalent in that they yield identical information about the relative order of $a_i$ and $a_j$. We therefore assume that all comparisons have the form $a_i \le a_j$.

## Decision Tree Model

A **decision tree** is a full binary tree (each node is either a leaf or has both children) that represents the comparisons between elements that are performed by a particular sorting algorithm operating on an input of a given size. Control, data movement, and all other aspects of the algorithm are ignored. For example:

```
             ____ 1:2 _____
            /              \
          (<=)             (>)
          /                  \
         /                    \
       2:3                    1:3
      /   \                  /   \
    (<=)  (>)              (<=)  (>)
    /       \              /       \
<1,2,3>      1:3      <2,1,3>       2:3
            /   \                  /   \
          (<=)  (>)              (<=)  (>)
          /       \              /       \
      <1,3,2>   <3,1,2>      <2,3,1>   <3,2,1>
```

A decision tree has each internal node annotated by $i: j$ for some $i$ and $j$ in the range $1 \le i$ and $j \le n$, where $n$ is the number of elements in the input sequence. We also annotate each leaf by a permutation $\left< \pi(1), \pi(2),...,\pi(n) \right>$. Indices in the internal nodes and leaves always refer to the original positions of the array elements at the start of the sorting algorithm. The execution of the comparison sorting algorithm corresponds to tracing a simple path from the root of the decision tree down to a leaf. Each internal node indicates a comparison $a_i \le a_j$. The left subtree then dictates subsequent comparisons once we know that $a_i \le a_j$, and the right subtree dictates subsequent comparisons when $a_i > a_j$. Arriving at a leaf, the sorting algorithm has established the ordering $a_{\pi(1)}, a_{\pi(2)},...,a_{\pi(n)}$. Because any correct sorting algorithm must be able to produce each permutation of its input, each of the $n!$ permutation on $n$ elements must appear as at least one of the leaves of the decision tree for a comparison sort to be correct. Furthermore, each of these leaves must be reachable from the root by a downward path corresponding to an actual execution of the comparison sort, or in other words, the leaves are "reachable". Thus, we only consider decision trees in which each permutation appears as a reachable leaf.

## A Lower Bound for the Worst Case

The length of the longest simple path from the root of a decision tree to any of its reachable leaves represents the worse-case number of comparisons that the corresponding sorting algorithm performs. As a result, the worst case number of comparisons for a given comparison sort algorithm equals the height of its decision tree. A lower bound on the heights of all decision trees in which each permutation appears as a reachable leaf is therefore a lower bound on the running time of any comparison sort algorithm. The following theorem establishes such a lower bound.

_**Theorem:** Any comparison sort algorithm requires_ $\Omega(n \lg n)$ _comparisons in the worst case_.

_**Corollary:** Heapsort and merge sort are asymptotically optimal comparison sorts_