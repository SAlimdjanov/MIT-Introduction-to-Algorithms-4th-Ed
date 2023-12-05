# Simple Array-Based Data Structures

## Arrays

Assume that (as in most languages), an array is stored as a contiguous sequence of bytes in memory. If the first element of an array has index $s$, the array starts at memory address $a$, and each array element occupies $b$ bytes, then the $i$-th element occupies bytes $a + b(i - s)$ through $a + b(i - s + 1) - 1$. Assuming the computer can access all memory locations in the same amount of time (as per the RAM model), it takes constant time to access any array element, regardless of the index.

Most programming languages require each element of a particular array to be the same size. If the elements of a given array might occupy a different number of bytes, the formulas above do not apply. In such cases, the array elements are usually objects of varying sizes, and what actually appears in each array element is a pointer to the object. The number of bytes occupied by a pointer is typically the same, no matter what the pointer references, so that to access an object in an array, the above formulas give the address of the pointer to the object and then the pointer must be followed to access the object itself.

## Matrices

Typically represented by a 2-D or multi-dimensional array. The two most common ways to store a matrix are row-major and column-major order. Consider an $m \times n$ matrix. In **row-major order**, the matrix is stored row by row, and in **column-major order**, the matrix is stored in a column.

$$M =
\left(\begin{matrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
\end{matrix}\right)
$$

Row-major order would be stored in a 1-D array as $[1, 2, 3, 4, 5, 6]$ or in a 2-D array as $[[1, 2, 3], [4, 5, 6]]$. Column-major order would be stored in a 1-D array as $[1, 4, 2, 5, 3, 6]$ or in a 2-D array as $[[1, 4], [2, 5], [3, 6]]$. Occasionally, other schemes are used to store matrices. In the **block representation**, the matrix is divided into blocks, and each block is stored contiguously.

$$
C=\left(
\begin{array}{c|c}
\begin{matrix} 1 & 2 \\ 5 & 6 \end{matrix} &
\begin{matrix} 3 & 4 \\ 7 & 8 \end{matrix} \\ 
\hline
\begin{matrix} 9 & 10 \\ 13 & 14 \end{matrix} &
\begin{matrix} 11 & 12 \\ 15 & 16 \end{matrix}
\end{array}\right)
$$

This can be stored in a 1-D array as $[1, 2, 5, 6, 3, 4, 7, 8, 9, 10, 13, 14, 11, 12, 15, 16]$.

## Stacks and Queues

Stacks and queues are dynamic sets in which the element removed from the set by the $\text{DELETE}$ operation is prespecified. In a **stack**, the element deleted from the set is the one most recently inserted: the stack implements a **last-in, first-out** or **LIFO** policy. Similarly, in a **queue**, the element deleted is always the one that has been in the set for the longest time: the queue implements a **first-in, first-out** or **FIFO** policy.

### Stacks

The $\text{INSERT}$ operation on a stack is often called $\text{PUSH}$, and the $\text{DELETE}$ operation, which does not take an element argument, is often called $\text{POP}$. These names are allusions to physical stacks, such as the spring-loaded stacks of plates used in cafeterias. The order in which the plates are popped from the stack is the reverse of the order in which they were placed onto the stack, since only the top plate is accessible.

A stack has attributes $S.top$, indexing the most recently inserted element, and $S.size$, equalling the size $n$ of the array. The stack consists of elements $S[1: S.top]$, where $S[1]$ is the element at the bottom of the stack and $S[S.top]$ is the element at the top. When $S.top = 0$, the stack contains no elements and is empty. We can test whether the stack is empty with a query operation $\text{STACK-EMPTY}$. Upon an attempt to pop an empty stack, the stack **underflows**, which is normally an error. If $S.top$ exceeds $S.size$, the stack **overflows**.

THe procedures `STACK_EMPTY`, `PUSH`, and `POP` implement each of the stack operations. Each of them take $O(1)$ time.

```python
STACK_EMPTY(S)
    if S.top == 0
        return True
    else
        return False

PUSH(S, x)
    if S.top == S.size
        error "Overflow"
    else
        S.top = S.top + 1
        S[S.top] = x

POP(S)
    if STACK_EMPTY(S)
        error "Underflow"
    else S.top = S.top - 1
        return S[S.top + 1]
```

### Queues

We call the $\text{INSERT}$ operation on a queue $\text{ENQUE}$, and we call the $\text{DELETE}$ operation $\text{DEQUEUE}$. Like the stack operation $\text{POP}$, $\text{DEQUEUE}$ takes no element argument. The FIFO property of a queue causes it to operate like a line of customers waiting for a service. The queue has a **head** and a **tail**. When an element is enqueued, it takes its place at the tail of the queue, just as a newly arriving customer always takes the place at the end of the line. The element dequeued is always at the head of the queue, like the customer who has waited the longest.

One way to implement a queue of at most $n - 1$ elements is using an array $Q[1: n]$m whith the attribute $Q.size$ equalling the size $n$ of the array. The queue has an attribute $Q.head$ that indexes (or points to) its head. The attribute $Q.tail$ indexes the next location at which a newly arriving element will be inserted into the queue. The elements in the queue reside in locations $Q.head$, $Q.head + 1, ..., Q.tail - 1$, where we "wrap around" in the sense that location $1$ immediately follows location $n$ in a circular order. When $Q.head = Q.tail$, the queue is empty. Initially, we have $Q.head = Q.tail = 1$. An attempt to dequeue an element from an empty queue causes the queue to underflow. When $Q.head = Q.tail + 1$ or both $Q.head = 1$ and $Q.tail = Q.size$, the queue is full, and an attempt the enqueue an element causes the queue to overflow.

The procedures `ENQUEUE` and `DEQUEUE` (with omitted error checking), each operation takes $O(1)$ time.

```python
ENQUEUE(Q, x)
    Q[Q.tail] = x
    if Q.tail == Q.size
        Q.tail = 1
    else
        Q.tail = Q.tail + 1

DEQUEUE(Q)
    x = Q[Q.head]
    if Q.head == Q.size
        Q.head = 1
    else
        Q.head = Q.head + 1
    return x
```
