# Open Addressing

In **open** addressing, all elements occupy the hash table itself. Each table entry contains either an element of the dynamic set or $\text{NIL}$. No lists or elements are stored outside the table, unlike in chaining. Thus, in open addressing, the hash table can "fill up" so that no further insertions can be made. One consequence is that the load factor $\alpha$ can never exceed $1$.

Collisions are handled as follows: when a new element is to be inserted into the table, it is placed in its "first-choice" location if possible. If that location is already occupied, the new element is placed in its "second-choice" location. The process continues until an empty slot is found in which to place the new element. Different elements have different preference orders for the locations. To search for an element, systematically examine the preferred table slots for that element, in order of decreasing preference, unitl you you either find the desired element or you find an empty slot and thus verify that the element is not in the table.

Of course, you could use chaining and store the linked lists inside the hash table, in the otherwise unused hash-table slots, but the advantage of open addressing is that it avoids pointers all together. Instead of following pointers, a sequence of slots to be examined is computed. The memory freed by storing pointers provides the hash table with a larger number of slots in the same amount of memory, potentially yielding fewer collisions and faster retrieval.

To perform insertion using open addressing, successively examine or **probe** the hash table until an empty slot is found for the key to be placed in. Instead of being fixed in the order $0, 1, ..., m - 1$ which implies a $\Theta(n)$ search time, the sequence of positions probed depends upon the key being inserted. To determine which slots to probe, the hash function includes the probe number (starting from $0$) as a second input. Thus the hash function becomes:

$$h: U \times \set{0, 1, ..., m - 1} \rightarrow \set{0, 1, ..., m - 1}$$

Open addressing requires that for every key $k$, the **probe sequence** $\left< h(k, 0), h(k, 1), ... h(k, m - 1)\right>$ be a permutation of $\set{0, 1, ..., m - 1}$ so that every hash-table position is eventually considered as a slot for a new key as the table fills up. The `HASH_INSERT` procedure assumes that the elements in the hash table $T$ are keys with no satellite information: the key $k$ is identical to the element containing the key $k$. Each slot contains either a key or $\text{NIL}$ if the slot is empty. The procedure takes as input a hash table $T$ and a key $k$ that is assumed to be not already present in the table. It either returns the slot number where it stores key $k$ or flags an error because the hash table is already full.

```python
HASH_INSERT(T, k)
    i = 0
    {repeat
        q = h(k, i)
        if T[q] == NIL
            T[q] = k
            return q
        else
            i = i + 1
    until i == m}
    error "hash table overflow"

HASH_SEARCH(T, k)
    i = 0
    {repeat
        q = h(k, i)
        if T[q] == k
            return q
        i = i + 1
    until T[q] == NIL or i == m}
    return NIL
```
