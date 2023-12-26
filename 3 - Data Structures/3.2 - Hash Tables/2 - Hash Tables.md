# Hash Tables

Using a direct-address table becomes impractical when the number of possible slots is large. When the set $K$ of keys stored in a dictionary is much smaller than the universe $U$ of all possible keys, a hash table requires much less storage than a direct-address table. Specifically, the space complexity is reduced to $\Theta(|K|)$ while maintaining the benefit that searching for an element in the hash table still only requires $O(1)$ time. The catch is that this bound is for the average-case time, whereas for direct addressing it holds for the worst-case time.

With direct addressing, an element with key $k$ is stored in slot $k$, but with hashing, we use a **hash function** $h$ to compute the solot number from the key $k$, so that each element goes into slot $h(k)$. The hash function $h$ maps the universe $U$ of keys into slots of a **hash table** $T[0:m - 1]$:

$$h: U \rightarrow \set{0, 1, ..., m - 1}$$

where the size $m$ of the hash table is typically much less than $|U|$. We say that an element with key $k$ **hashes** to slot $h(k)$ and we also say that $h(k)$ is the **hash value** of key $k$. An (not great) example of a hash function is $h(k) = k \text{ mod } m$. There are situations where two keys may hash to the same slot, namely a **collision**. Fortunately, there are techniques that can be employed to mitigate collisions.

## Independent Uniform Hashing

An ideal hash function would have, for each possible input $k$ in the domain $U$, an output h(k) that is an element randomly and independently chosen uniformly from the range $\set{0, 1, ..., m - 1}$. Once a value $h(k)$ is randomly chosen, each subsequent call to $h$ with the same input $k$ yields the same output $h(k)$. Such an ideal hash function is called an **independent uniform hash function**. Such a function is also often called a **random oracle**. When hash tables are implemented with an independent uniform hash function, we are using **independent uniform hashing**. This concept is an ideal theoretical abstraction, and is not easy to implement in practice. The next sections present techniques to achieve practical approximations.

## Collision Resolution by Chaining

One can think of hashing with chaining as a nonrecursive form of divide-and-conquer: the input set of $n$ elements is divided randomly into $m$ subsets, each of approximate size $n / m$. A hash function determines which subset an element belongs to. Each subset is managed independently as a list. The idea of **chaining**: Each non-empty slot points to a linked list, and all the elements that hash to the same slot go into that slot's linked list. Slot $j$ contains a pointer to the head of the list of all stored elements with hash value $j$. If there are no such elements, then slot $j$ contains $\text{NIL}$.

When collisions are resolved by chaining, the dictionary operations are straight-forward to implement. The worst-case running time for insertion is $O(1)$. Deletion takes $O(1)$ time if the lists are doubly linked.

```python
CHAINED_HASH_INSERT(T, x)
    LIST_PREPEND(T[h(x.key)], x)

CHAINED_HASH_SEARCH(T, k)
    return LIST_SEARCH(T[h(k)], k)

CHAINED_HASH_DELETE(T, x)
    LIST_DELETE(T[h(x.key)], x)
```

### Analysis of Hashing with Chaining

Given a hash table $T$ with $m$ slots that stores $n$ elements, we define the **load factor** $\alpha$ for $T$ as $n / m$, that is, the average number of elements stored in a chain. The analysis will be in terms of $\alpha$, which is less than, equal to, or greater than $1$.

The worst-case behavior of hashing with chaining is terrible: all $n$ keys hash to the same slot, creating a list of length $n$, the worst-case time for searching is thus $\Theta(n)$ plus the time it takes to compute the hash function (no better than using one linked list for all elements). The average case performance of hashing depends on how well the hash function $h$ distributes the set of keys to be stored among the $m$ slots. For now, assume that the hash function is **uniform**. Further assume that where a given element hashes to is _independent_ of where elements hash to, in other words, in this section **independent uniform hashing** is used.

Because hashes of distinct keys are assumed to be independent, independent uniforma hashing is **universal**: the chance that any two distinct keys $k_1$ and $k_2$ collite is at most $1 / m$. Universality is important in the analysis and is also in the specification of universal families of hash functions. For $j = 0, 1, ..., m - 1$, denote the length of the list $T[j]$ by $n_j$, so that $n = n_0 + n_1, ..., n_{m - 1}$ and the expectation value of $n_j$ is $E[n_j] = \alpha = n / m$.

Assume that $O(1)$ time suffices to compute the hash value $h(k)$, so that the time required to search for an element with $k$ depends linearly on the length $n_{h(k)}$ of the list $T[h(k)]$. Setting aside the $O(1)$ time required to compute the hash function and to access slot $h(k)$, we'll consider the expected number of elements examined by the search algorithm, that is, the number of elements in the list $T[h(k)]$ that the algorithm checks to see whether any have a key equal to $k$. We consider two cases. In the first, the search is unsuccessful: no element in the table has key $k$. In the second, the search successfully finds the element with key $k$.

_**Theorem:** In a hash table in which collisions are resolved by chaining, an unsuccessful search takes_ $\Theta(1 + \alpha)$ _time on average, under the assumption of independent uniform hashing_.

_**Theorem:** In a hash table in which collisions are resolved by chaining, a successful search takes_ $\Theta(1 + \alpha)$ _time on average, under the assumption of independent uniform hashing_.

If the number of elements in the table is at most proportional to the number of hash-table slots, we have $n = O(m)$ and consequently, $\alpha = n / m = O(m) / m = O(1)$. Thus, searching takes constant time on average. Since insertion takes $O(1)$ worse-case time and deletion takes $O(1)$ worst-case time when the lists are doubly linked (assume the list element object is known, and not just its key), we can support all dictionary operations in $O(1)$ time on average.
