# Insertion Sort

**Sorting Problem:** you neeed to sort a sequence of numbers into monotonically increasing order. **Insertion Sort** solves this problem.

---

#### Input

A sequence of $n$ numbers $\langle{a_1, a_2, ... , a_n}\rangle{}$

#### Output

A permutation $\langle{a_1^{'}, a_2^{'}, ... , a_n^{'}}\rangle{}$ of the input sequence such that $a_1^{'} < a_2^{'} < ... < a_n^{'}$.

---

The numbers to be sorted are known as **keys**. The input comes in the form of an array with $n$ elements. When we want to sort numbers, it is often because the keys are associated with other data, which we call **satellite data**. Together, key and satellite data form a **record**.

**Insertion Sort:** An efficient algorithm for sorting a small number of elements. Think of a pile of blocks numbered from $1$ to $n$:

1.  Start with an empty left hand and the blocks in a pile on the table
2.  Pick up the first block and hold it in your left hand
3.  With your right hand, remove one block from the pile and insert it into the correct position in your left hand
4.  If all blocks in your left hand have values greater than the card in your right hand, pace this block as the leftmost block in your left hand

At all times, the blocks held in your left hand hare sorted, and these blocks were originally the top blocks of the pile on the table.

#### Pseudocode

```python
INSERTION-SORT(A, n)
    for i = 2 to n
        key = A[i]
        # Insert A[i] into the sorted subarray A[1:i - 1]
        j = i - 1
        while j > 0 and A[j] > key
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key
```

At the beginning of each iteration of the `for` loop, (indexed by `i`, the current block) the **subarray** (a contiguous portion of the array) consisting of elements `A[1:i - 1]` constitutes the currently sorted blocks, and the remaining subarray `A[i + 1:n]` corresponds to the pile still on the table.

Elements `A[1:i - 1]` are the elements originally in positions $1$ through $i-1$, but now in sorted order. The properties of these elements can be stated formally as a **Loop Invariant**:

-   At the start of each iteration of the `for` loop of lines 1 to 8, the subarray `A[1:i - 1]` consists of the elements originally in `A[1:i - 1]`, but in a sorted order.

Loop invariants help us understand why an algorithm is correct. When using them, you need to show:

1.  **Initialization:** It is true prior to the first iteration of the loop
2.  **Maintenence:** If it is true prior to an iteration of the loop, it remains true before the next iteration
3.  **Termination:** The loop terminates, and when it terminates, the invariant (usually along with the reason it terminated) gives a useful property to show the algorithm is correct
