# Representing Rooted Trees

## Binary Trees

Use attributes $p$, $left$, and $right$ to store pointers to the parent, left child, and right child of each node in a binary tree $T$. If $x.p = \text{NIL}$, then $x$ is the root. If node $x$ has no left child, then $x.left = \text{NIL}$, and similarly for the right child. The root of the entire tree $T$ is pointed to by the attribute $T.root$. If $T.root = \text{NIL}$, the tree is empty.

## Rooted Trees with Unbounded Branching

It is simple to extend the scheme for representing a binary tree to any class of trees in which the number of children of each node is at most some constant $k$: replace the $left$ and $right$ attributes by $child_1, child_2,..., child_k$. This scheme no longer works when the number of children of a node is unbounded, however, since we do not know how many attributes to allocate in advance. If $k$, the number of children, is bounded by a large constant but most nodes have a small number of children, we may waste a lot of memory.

Fortunately, there is a clever scheme to represent trees with arbitrary numbers of children. It has the advantage of using only $O(n)$ space for any $n$-node rooted tree. The **left-child, right-sibling representation** is as follows. As before, each node contains a parent pointer $p$, and $T.root$ points the the root of the tree $T$. Instead of having a pointer to each of its children, each node $x$ has only two pointers:

1.  $x.leftchild$ points to the leftmost child of node $x$
2.  $x.rightsibling$ points to the sibling of $x$ immediately to its right

If node $x$ has no children, then $x.leftchild = \text{NIL}$, and if node $x$ is the rightmost child of its parent, then $x.rightsibling = \text{NIL}$

## Other Tree Representations

Trees can be represented in other ways. Recall heaps, which is based on a complete binary tree. Many other schemes are possible, and which is best depends on the application.
