# Analyzing Algorithms

Analysis of algorithms involves considering consumption of resources such as memory, communication bandwith, and computational time.

**RAM (Random-Acces Machine) Model:** The generic one-processor model of computation:

-   Instructions execute one after another (no simultaneous processing)
-   Assumes each instruction takes the same amount of time as any other instruction and that each data access (using the value of a variable or storing into a variable) takes the same amount of time as any other data access
-   Contains operations found in real computers:
    -   Arithmetic (add, subtract, divide, remainder, floor, ceiling, etc.)
    -   Data movement (load, store, copy, etc.)
    -   Control (conditionals, subroutine call and return, etc.)
-   Data types are int, float, and char (bools are 0 or 1)

**Note:** This model is obviously unrealistic as modern machines contain multiple processing cores and multi-threading capabilities. It serves the purpose of algorithmic analysis.

### Example Analysis - Insertion Sort Algorithm

Running time depends on the size of the input. Some important definitions:

-   **Input Size:** This can vary based on the nature of the algorithm. The most natural measure is the total number of bits needed to represent the input in ordinary binary notation
-   **Running Time:** The number of instructions and data accesses executed

Accounting for these costs is independent of the computer as it is within the RAM model. Let's adopt the following view:

-   A constant amount of time is required to execute each line of the pseudocode
-   One line might take more/less time than the other, but assume that each execution of the $k\text{th}$ line to be $c_k$ (constant) time

This view satisfies the RAM model, and it also reflects how the pseudocde would be implemented on most actual computers.

For each $i = 2, 3, ..., n$, let $t_i$ denote the number of times the `while` loop test in line 5 is executed for that value of $i$.

The running time of the algorithm is the sum of the running times for each statement executed. A statement that takes $c_k$ steps to execute and executes $m$ times contributes $c_km$ to the total running time. $T(n)$ denotes the running time of an algorithm on an input of size $n$. To compute $T(n)$, calculate the sum of the products of the costs and times:

| Line | `INSERTION_SORT(A,N)`        | Cost  | Time                            |
| ---- | ---------------------------- | ----- | --------------------------------|
| 1    | `for i = 2 to n`             | $c_1$ | $n$                             |
| 2    | `key = A[i]`                 | $c_2$ | $n-1$                           |
| 4    | `j = i - 1`                  | $c_4$ | $n - 1$                         |
| 5    | `while j > 0 and A[j] > key` | $c_5$ | $\sum\limits_{i=2}^n t_i$       |
| 6    | `A[j + 1] = A[j]`            | $c_6$ | $\sum\limits_{i=2}^n (t_i - 1)$ |
| 7    | `j = j - 1`                  | $c_7$ | $\sum\limits_{i=2}^n (t_i - 1)$ |
| 8    | `A[j + 1] = key`             | $c_8$ | $n - 1$                         |

**Note:** Line 3 is omitted as it is a comment.

Even for inputs of a given size, an algorithm's running time may depend of which input of that size is given. For example, in `INSERTION_SORT`, the best case occurs when the array is already sorted. Here, each time line 5 executes, the value of `key` is already greater than or equal to all values in `A[1:i - 1]`, so that the `while` loop of lines 5-7 always exits upon the first test in line 5. Therefore, $t_i = 1$ for each value of $i$, and the best case running time is:

$$
\begin{align*}
T(n) &= c_1n + c_2(n-1) + c_4(n-1) + c_5(n-1) + c_8(n-1) \\
&= c_1n + c_2(n-1) + c_4(n-1) + c_5(n-1) + c_8(n-1) \\
&= c_kn - c_k
\end{align*}
$$

The best-case running time is thus linear. The worst case arises when the input array is sorted in the reverse order. The procedure must compare each element `A[i]` with each element in the entire sorted subarray `A[1:i - 1]`, and so $t_i = i$ for $i = 2, 3, ..., n$. The procedure finds that `A[j] > key` every time in line 5, and the `while` loop exits only when `j` reaches 0:

$$
\begin{align*}
\sum\limits_{i=2}^n{i} &= \left(\sum\limits_{i=1}^{n}{i}\right) - 1 \\
&= \frac{n(n+1)}{2} - 1 \\
\end{align*}
$$

$$
\begin{align*}
\sum\limits_{i=2}^{n}{(i - 1)} &= \left(\sum\limits_{i=1}^{n - 1}{i}\right) - 1 \\
&= \frac{n(n+1)}{2} \\
\end{align*}
$$

Performing the computation of $T(n)$ yields:

$$
\begin{align*}
T(n) &= c_1n + c_2(n-1) + c_4(n-1) + c_5\left(\frac{n(n+1)}{2}-1\right) + c_6\left(\frac{n(n+1)}{2}\right) + c_7\left(\frac{n(n+1)}{2}\right)+ c_8(n-1) \\
\end{align*}
$$

By inspection, one can see that the worst-case $T(n)$ is quadratic. We usually concentrate on only finding the worst-case time, for the following reasons:

1.  The worst-case running time of an algorithm gives an upper bound on the running time of _any_ input
2.  For some algorithms, the worst case occurs fairly often
3.  The average case is often as bad as the worst case

#### Order of Growth

Also known as the **Rate of Growth**, is the leading term of a computed $T(n)$, since the lower order terms are neglible. To highlight the order of growth of the running time, we utilize $\Theta$ notation. For the previous example, we write that the algorithm has $\Theta(n^2)$ running time growth.
