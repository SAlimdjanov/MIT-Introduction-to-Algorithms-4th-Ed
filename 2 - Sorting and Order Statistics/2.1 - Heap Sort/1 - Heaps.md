# Heaps

The **binary heap** data structure is an array object that we can view as a nearly complete binary tree. Each node of the tree corresponds to an element in the array. The tree is completely filled up on all levels except possibly the lowest.

An array $A [1: n]$ represents a heap as an object with an attribute `A.heap_size` which represents how many elements in the heap are stored within an array $A$. Although $A[1: n]$ may contain numbers, only the elements in `A[1: A.heap_size]` where $0 \le$ `A.heap_size` $\le n$ are valid elements of the heap. If heap size is $0$, the heap is empty.

```python
    # 0,  1,  2, 3, 4, 5, 6, 7, 8, 9
A = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
```

```powershell
        16        # 0
        / \
       /   \
      /     \
     /       \
    14       10    # 1, 2
   /  \     /  \
  8    7   9    3  # 3, 4, 5, 6
 / \   |
2   4  1           # 7, 8, 9
```

The root of the tree is `A[0]`, and given the index $i$ of a node, there's a simple way to compute the indices of its parent, left child, and right child with the on-line procedures below:

```python
PARENT(i)
    return floor(i / 2)

LEFT(i)
    return 2i

RIGHT(i)
    return 2i + 1
```

There are two kinds of binary heaps: max-heaps and min-heaps. In both kinds, the values in the nodes satisfy a **Heap property**, the specifics of which depend on the kind of heap. In a **max-heap**, the **max-heap property** is that for every node $i$ other than the root:

$$A[\text{PARENT(i)]} \ge A[i]$$

The **min-heap property** is the opposite:

$$A[\text{PARENT(i)]} \le A[i]$$

The heapsort algorithm uses max-heaps. Min-heaps commonly implement priority queues. Viewing the heap as a tree, we define the **height of a node** in a heap to be the number of edges on the longest simple downward path from the node to a leaf, and we define the **height of a heap** to be 