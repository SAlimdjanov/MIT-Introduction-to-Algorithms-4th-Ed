# Direct Address Tables

Direct addressing is a simple technique that works well when the universe $U$ of keys is reasonably small. Suppose that an application needs a dynamic set in which each element has a distinct key drawn from the universe $U = \set{0, 1, ..., m - 1}$, where $m$ is not too large.

To represent the dynamic set, you can use an array, or **direct-address table**, denoted by $T[0: m - 1]$, in which each **slot** corresponds to a key in the universe $U$. Slot $k$ points to an element in the set with key $k$. If the set contains no element with key $k$, then $T[k] = \text{NIL}$.

The dictionary operations $\text{DIRECT-ADDRESS-SEARCH}$, $\text{DIRECT-ADDRESS-INSERT}$, and $\text{DIRECT-ADDRESS-DELETE}$ are trivial to implement and take $O(1)$ time. For some applications, the direct-table itself can hold the elements in the dynamic set. That is, rather than storing an element's key and satellite data in an object external to the direct address table, with a pointer from a slot in the table to an object, save space by storing the object directly in the slot. To indicate an empty slot, use a special key. Why store the key of the object at all? The index of the object is its key! (Well, one needs a way to denote an empty slot)

```python
DIRECT_ADDRESS_SEARCH(T, k)
    return T[k]

DIRECT_ADDRESS_INSERT(T, x)
    T[x.key] = x

DIRECT_ADDRESS_DELETE(T, x)
    T[x.key] = NIL
```