# Priority Queues

This is one of the most popular applications of the heap data structure. As with heaps, they come in two forms: maximum and minimum priority queues.

A **priority queue** is a data structure for maintaining a set of $S$ elements, each with an associated value called a **key**. A **max-priority queue** supports the following operations:

-   $\text{INSERT} (S, x, k)$ inserts the element $x$ with key $k$ into the set $S$, which is equivalent to the operation $S = S \cup \set{x}$
-   $\text{MAX} (S)$ returns the element of $S$ with the largest key
-   $\text{EXTRACT-MAX} (S)$ removes and returns the element of $S$ with the largest key
-   $\text{INCREASE-KEY} (S, x, k)$ increases the value of element $x$'s key to the new value $k$, which is assumed to be at least as larges as $x$'s current key value

One can apply max-priority queues to schedule jobs on a computer shared among multiple users, as it keeps track of the jobs to be performed and their relative priorities. When a job is finished or interrupted, the scheduler selects the higher-priority job from among those pending by calling $\text{EXTRACT-MAX}$. The scheduler can then add a new job to the queue at any time by calling $\text{INSERT}$. Alternatively, a **min-priority queue** supports the operations $\text{INSERT, MIN, EXTRACT-MIN,}$ and $\text{DECREASE-KEY}$.

When you use a heap to implement a priority queue within a given application, elements of the priority queue correspond to objects in the application. Each object contains a key. If the priority queue is implemented by a heap, you need to determine which application object corresponds to a given heap element, and vice versa. Because heap elements are stored in an array, you need a way to map application objects to and from array indices. Here are two methods to accomplish this:
-   Utilizing handles
-   Hash table

## Implementation

The procedure `MAX_HEAP_MAXIMUM` implements the $\text{MAX}$ operation in $\Theta (n)$ time.

```
MAX_HEAP_MAXIMUM(A)
    if A.heap_size < 1
        error "Heap underflow"
    return A[1]
```

`MAX_HEAP_EXTRACT_MAX` implements the operation $\text{EXTRACT-MAX}$ in $O(\lg n)$ time. We implicitly assume that `MAX_HEAPIFY` compares priority queue objects based on their key attributes. Additionally, assume that when `MAX_HEAPIFY` exchanges elements in the array, it is exchanging pointers and also that it updates the mapping between objects and array indices.

```
MAX_HEAP_EXTRACT_MAX(A)
    max_elem = MAX_HEAP_MAXIMUM(A)
    A[1] = A[A.heap_size]
    A.heap_size = A.heap_size - 1
    MAX_HEAPIFY(A, 1)
    return max_elem
```

The procedure `MAX_HEAP_INCREASE_KEY` implements the $\text{INCREASE-KEY}$ operation. It first verifies that the new key $k$ will not cause the key in the object $x$ to decrease, and if there is no problem, it gives $x$ the new key value. It then finds the index $i$ in the array corresponding to object $x$, so that $A[i]$ is $x$. Because increasing the key of $A[i]$ might violate the max-heap property, the procedure then, similarly to `INSERTION_SORT`, traverses a simple path from this node torward the root to find a proper place for the newly increased key. As `MAX_HEAP_INCREASE_KEY` traverses this path, it repeatedly compares an element's key to that of its parent, exchanging pointers and continuing if the element's key is larger, and terminating if the key is smaller, since the max-heap property now holds. Like `MAX_HEAPIFY` when used in a priority queue, `MAX_HEAP_INCREASE_KEY` updates the information that maps objects to array indices when array elements are exchanged. In addition to the overhead for mapping priority queue objects to array indices, the running time of this procedure on an $n$-element heap is $O(\lg n)$, since the path from the node updated in line 3 has length $O(\lg n)$.

```
MAX_HEAP_INCREASE_KEY(A, x, k)
    if k < x.key
        error "New key is smaller than current key"
    x.key = k
    find the index i in array A where object x occurs
    while i > 1 and A[PARENT(i)].key < A[i].key
        exchange A[i] with A[PARENT(i)], updating the information that maps priority queue objects to array indices
        i = PARENT(i)
```

The procedure `MAX_HEAP_INSERT` implements the $\text{INSERT}$ operation. It takes array $A$ implementing the max-heap, the new object $x$ to be inserted into the max-heap, and size $n$ of array $A$ as inputs. The procedure first verifies that the array has room for the new element. It then expands the max-heap by adding to the tree a new leaf whose key is $-\infty$. Then it calls `MAX_HEAP_INCREASE_KEY` to set the key of this new element to its correct value and maintain the max-heap property. The running time of this procedure is $O(\lg n)$ plus the overhead for mapping priority queue objects to indices.

```
MAX_HEAP_INSERT(A, x, n)
    if A.heap_size == n
        error "Heap overflow"
    A.heap_size = A.heap_size + 1
    k = x.key
    x.key = -inf
    A[A.heap_size] = x
    map x to index heap_size in the array
    MAX_HEAP_INCREASE_KEY(A, x, k)
```

In summary, a heap can support any priority-queue operation on a set of size $n$ in $O(\lg n)$ time, plus overhead mapping from priority queue objects to array indices.