# $O$-Notation, $\Omega$-Notation, and $\Theta$-Notation

## $O$-Notation

This characterizes an upper bound on the asymptotic behavior of a function. In other words, it says that a function grows no faster than a certain rate, based on the highest-order term. (I have already used this in the programs I have written thus far)

#### Example

Consider the function $7 n^3 + 100 n^2 - 20 n + 6$. The highest-order term is $7 n^3$, so the growth rate is $n^3$. One can then write that this is $O(n^3)$.

## $\Omega$-Notation

This characterizes a lower bound on the asymptotic behavior of a function. In other words, it says that a function grows at least as fast as a certain rate, based on the highest-order term

#### Example

Consider the function used in the previous example. We can say that the function is $\Omega(n^3)$, but it is also $\Omega(n^2)$ and $\Omega(n)$. In general, it is $\Omega(n^c)$ for any constant $c \le 3$.

## $\Theta$-Notation

This characterizes a tight bound on the asymptotic behavior of a function. In other words, it says that a function grows precisely a certain rate, based on the highest-order term. This notation characterizes the rate of growth to within a constant factor from above and to within a constant factor from below. These two factors cannot be equal. If you can show that a function is both $O(f(n))$ and $\Omega(f(n))$ for some function $f(n)$, then you have shown that the function is $\Theta(f(n))$.

#### Example

Considering the previous two examples, the function is $O(n^3)$ and $\Omega(n^3)$. Therefore, it is $\Theta(n^3)$.

### Revisiting Insertion Sort

```python
INSERTION_SORT(A, n)
    for i = 2 to n
        key = A[i]
        # Insert A[i] into the sorted subarray A[1:i - 1]
        j = i - 1
        while j > 0 and A[j] > key
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key
```

The outer loop runs $n - 1$ times regardless of how the array is sorted and the inner loop iterates depending on the input. The loop variable $j$ starts at $i - 1$ and decreases until the condition is met. For a given value of $i$, the while loop might not iterate at all, $i - 1$ times, or anywhere in between. These observtions suffice to deduce an $O(n^2)$ running time, is it covers all input scenarios.

We can also see that the worst-case running time is $\Omega(n^2)$ when we consider the maximum number of iterations of both loops. This measn that for every $n$ sized input above a certain threshold, there is at least one input of size $n$ for which the algorithm takes at least $c n^2$ time, for some positive constant $c$.

Therefore, we can conclude that Insertion Sort is $\Theta(n^2)$. It does not matter what the constant factors for upper and lower bounds might differ. What matters is that we have characterized the worst-case running time to within constant factors (discounting lower-order terms). This argument does not show that Insertion Sort runs in $\Theta(n^2)$ time in all cases.
