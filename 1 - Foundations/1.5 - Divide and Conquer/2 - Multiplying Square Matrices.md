# Multiplying Square Matrices

Let $A = (a_{ik})$ and $B = (b_{jk})$ be square $n \times n$ matrices. The matrix product $C = A \cdot B$ is also an $n \times n$ matrix:

$$ c_{ij} = \sum\limits_{k = 1}^n a_{ik} \cdot b_{kj}$$

## Naive Algorithm

Generally, assume that the matrices are **dense**, meaning that most of the $n^2$ entries are not $0$ as opposed to **sparse**. The procedure `MATRIX_MULTIPLY_NAIVE` is below:

```python
MATRIX_MULTIPLY(A, B, C, n)
    for i = 1 to n
        for j = 1 to n
            for k = 1 to n
                c_ij = c_ij + a_ik * b_kj
```

If only the product $A \cdot B$ is needed, just initialize all $n^2$ to 0 before calling the procedure, which takes an additional $\Theta(n^2)$ time. The cost of matrix multiplication asymptotically dominates this initialization cost. The naive implementation runs in $\Theta(n^3)$ time.

## A Simple Divide-and-Conquer Algorithm

For $n > 1$, the divide step partitions the $n \times n$ matrices into four $(n / 2) \times (n / 2)$ submatrices. We'll assume that $n$ is an exact power of $2$, so that as the algorithm recurses, we are guaranteed that the submatrix dimensions are integer.

The `MATRIX_MULTIPLY_RECURSIVE` procedure implements a divide-and-conquer strategy for square matrix multiplication:

```python
MATRIX_MULTIPLY_RECURSIVE(A, B, C, n)
    if n == 1
    # Base case
        c_11 = c_11 + a_11 * b_11
        return
    # Divide
    '''Partition A, B, and C into (n/2) by (n/2) submatrices'''
    # Conquer
    MATRIX_MULTIPLY_RECURSIVE(A_11, B_11, C_11, n / 2)
    MATRIX_MULTIPLY_RECURSIVE(A_11, B_12, C_12, n / 2)
    MATRIX_MULTIPLY_RECURSIVE(A_21, B_11, C_21, n / 2)
    MATRIX_MULTIPLY_RECURSIVE(A_21, B_12, C_22, n / 2)
    MATRIX_MULTIPLY_RECURSIVE(A_12, B_21, C_11, n / 2)
    MATRIX_MULTIPLY_RECURSIVE(A_12, B_22, C_12, n / 2)
    MATRIX_MULTIPLY_RECURSIVE(A_22, B_21, C_21, n / 2)
    MATRIX_MULTIPLY_RECURSIVE(A_22, B_22, C_22, n / 2)
```

Omitting the base case, the recurrence for the running time of the above procedure is:

$$T(n) = 8 T(n / 2) + \Theta(1) $$

Via the master theorem, this also evaluates to $\Theta(n^3)$ time. This is because the nodes in the recursion tree for this procedure containing eight children.