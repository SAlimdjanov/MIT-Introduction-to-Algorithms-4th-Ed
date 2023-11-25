# Building a Heap

The procedure `BUILD_MAX_HEAP` converts an array `A[1:n]` into a max heap by calling `MAX_HEAPIFY` in a bottom-up (recursive) manner. The elements in the subarray `A[floor(n/2) + 1: n]` are all leaves of the tree, and so each is a one-element heap to begin with. It goes through the remaining nodes of the tree and runs the max heapify procedure on each of them:

```python
BUILD_MAX_HEAP(A, n)
    A.heap_size = n
    for i = floor(n / 2) down to 1
        MAX_HEAPIFY(A, i)
```

## Explanation

We can see how this works correctly through the following loop invariant:

**Loop Invariant - Definition:** At the start of each iteration of the `for` loop, each node `i + 1`, `i + 2, ..., n` is the root of a max-heap. Therefore:

-   **Initialization:** Prior to the first iteration of the loop, $i = \lfloor n / 2 \rfloor$. Each node $\lfloor n / 2 \rfloor + 1, \lfloor n / 2 \rfloor + 2,...,n $ is a leaf and this is the root of a trivial max-heap.

-   **Maintenance:** To see that each iteration maintains the loop invariant, observe that children of the node $i$ are numbered higher than $i$. By definition of the loop invariant, they are therefore both roots of max-heaps. This is the condition required for the recursive call, to make a node $i$ a max-heap root. Moreover, the `MAX_HEAPIFY` call preserves the property that the nodes are all roots of max-heaps. Decrementing $i$ in the `for` loop update re-establishes the loop invariant for the next iteration.

-   **Termination:** The loop makes exactly $\lfloor n / 2 \rfloor$ iterations, so it terminates. At termination, `i = 0`. By the loop invariant, each node $1, 2, ..., n$ us the root of a max-heap. In particular, node 1 (index 0 of the input array) is the root.

## Analysis

Each call to `MAX_HEAPIFY` costs $O( \lg n)$ time,  `BUILD_HEAP` makes $O(n)$ such calls. Thus the running time is simply $O(n) \cdot O( \lg n) = O(n \lg n)$. This upper bound, though correct, is not as tight as can be. This can be considered an 'average' case which is fine more more surface-level analyses.

We can derive a tighter asymptotic bound by observing that the time for `MAX_HEAPIFY` to run at a node varies with the height of the node in the tree, and that the heights of most nodes are small. A tighter analysis relies on the properties:

-   An $n$-element heap has height $\lfloor \lg n \rfloor$
-   At most, there are $\lceil n / 2^{h + 1} \rceil$ nodes of any height $h$

The time required by `MAX_HEAPIFY` when called on a node of height $h$ is $O(h)$. Letting $c$ be the constant implicit in the asymptotic notation, we can express the total cost of `BUILD_MAX_HEAP` as being bounded from above by:

We have $\lceil n / 2^{h + 1} \rceil \ge 1 / 2$ for $0 \le h \le  \lfloor \lg n \rfloor$. Since $\lceil x \rceil \le 2 x$ for any $x \ge 1 / 2$, we have:

$$\left\lceil \frac{n}{2^{h + 1}} \right\rceil \le \frac{n}{2^h}$$

From the appendices, with $x = 1 / 2$, we have the following relation, where $|x| < 1$:

$$\sum \limits_{k = 0} ^ {\infty} {k x^k} = \frac{x}{(1 - x)^2}$$


Which is results from differentiating the infinite geometric series and multiplying by $x$ From this, one can obtain:

$$
\begin{align*}
\sum \limits_{h = 0} ^ {\lfloor \lg n \rfloor} {\left\lceil \frac{n}{2^{h + 1}} \right\rceil c h} &\le c n \cdot \frac{1 / 2}{(1 - 1 / 2)^2} \\
&= O(n)
\end{align*}
$$

Hence, we can build a max-heap from an unordered array in linear time. To build a min-heap, use the procedure `BUILD_MIN_HEAP`, which is the same as `BUILD_MAX_HEAP`, with the recursive call being replaced by `MIN_HEAPIFY`. `BUILD_MIN_HEAP` produces a min-heap from an unordered linear array in linear time.

**Note:** See the `Code` folder in this section of the repository for the implementation of the above-mentioned procedures.

