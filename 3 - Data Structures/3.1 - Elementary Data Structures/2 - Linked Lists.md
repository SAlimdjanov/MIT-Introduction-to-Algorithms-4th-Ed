# Linked Lists

A **linked list** is a data structure in which the objects are arranged in a linear order. Unlike an array however, in which the linear order is determined by the array indices, the order in a linked list is determined by a pointer in each object. Since the elements of linked lists often contain keys that can be searched for, linked lists are sometimes called **search lists**. Linked lists provide a simple, flexible representation for dynamic sets, supporting (not necessarily efficiently) operations $\text{SEARCH}$, $\text{INSERT}$, $\text{DELETE}$, $\text{MINIMUM}$, $\text{MAXIMUM}$, $\text{SUCCESSOR}$, and $\text{PREDECESSOR}$.

Each element of a **doubly linked list** $L$ is an object with an attribute $key$ and two pointer attributes $next$ and $prev$. The object may contain other satellite data. Given an element $x$ in the list, $x.next$ points to its successor in the linked list, and $x.prev$ points to its predecessor. If $x.prev = \text{NIL}$, the element $x$ has no predecessor and is therefore the first element, or **head**, of the list. If $x.next = \text{NIL}$, the element has no successor and is therefore the last element, or **tail** of the list. An attribute $L.head$ points to the first element of the list. If $L.head = \text{NIL}$, the list is empty.

A list may have one of several forms. It may be either singly linked or doubly linked, it may be sorted or not, and it may be circular or not. If a list is **singly linked**, each element has a $next$ pointer but not a $prev$ pointer. If a list is **sorted**, the linear order of the list corresponds to the linear order of the keys stored in elements of the list. The minimum element is then the head of the list, and the maximum element is the tail. If the list is **unsorted**, the the elements can appear in any order. In a **circular list**, the $prev$ pointer points of the head of the list points to the tail, and the $next$ pointer of the tail points to the head. You can think of a circular list as a ring of elements. In the remainder of this section, we assume that the lists we are working with are unsorted and doubly linked.

## Searching a Linked list

The procedure `LIST_SEARCH` finds the first element with key $k$ in list $L$ by a simple linear search, returning a pointer to this element. If no object with key $k$ appears in the liist, then the procedure returns $\text{NIL}$. To search a list of $n$ objects, the procedure takes $\Theta(n)$ time in the worst case, since it may have to search the entire list.

```powershell
LIST_SEARCH(L, k)
    x = L.head
    while x != NIL and x.key != k
        x = x.next
    return x
```

## Inserting into a Linked List

Given an element $x$ whose $key$ attribute has already been set, the `LIST_PREPEND` procedure adds $x$ to the front of the linked list. Our attribute notation can cascade, so that $L.head.prev$ denotes the $prev$ attribute of the object that $L.head$ points to. The running time for the procedure on a list of $n$ elements is $O(1)$

```powershell
LIST_PREPEND(L, k)
    x.next = L.head
    x.prev = NIL
    if L.head != NIL
        L.head.prev = x
    L.head = x
```

You can insert anywhere within a linked list. If you have a pointer $y$ to an object in the list, the `LIST_INSERT` procedure "splices" a new element $x$ into the list, immediately following $y$, in $O(1)$ time. Since `LIST_INSERT` never references the list object $L$, it is not supplied as a parameter.

```powershell
LIST_INSERT(x, y)
    x.next = y.next
    x.prev = y
    if y.next != NIL
        y.next.prev = x
    y.next = x
```

## Deleting from a Linked List

The procedure `LIST_DELETE` removes an element $x$ from a linked list $L$. It must be given a pointer to $x$, and then "splices" $x$ out of the list by updating pointers. The delete an element with a given key, first call `LIST_SEARCH` to retrieve a pointer to the element. `LIST_DELETE` runs in $O(1)$ time, but to delete an element with a given key, the call to list search makes the worst-case running time to be $\Theta(n)$

```powershell
LIST_DELETE(L, x)
    if x.prev != NIL
        x.prev.next = x.next
    else
        L.head = x.next
    if x.next != NIL
        x.next.prev = x.prev
```

Insertion and deletion are faster operations on linked lists than on arrays. If you want to insert a new element into an array or delete the first element in the array, maintaining the relative order of all the existing elements, then each of the existing elements need to be moved by one position. In the worst case, insertion and deletion take $\Theta(n)$ time in an array, compared to $O(1)$ in a linked list. If you want to find the $k$-th element in the linear order, it takes just $O(1)$ time an any array regardless of $k$, but in a linked list, you'd have to traverse $k$ elements, taking $\Theta(k)$ time.

## Sentinels

The code for `LIST_DELETE` becomes simpler if you ignore the boundary conditions at the head and tail of the list:

```powershell
LIST_DELETE(x)
    x.prev.next = x.next
    x.next.prev = x.prev
```

A **sentinel** is a dummy object that allows us to simplify boundary conditions. In a linked list $L$, the sentinel is object $L.nil$ that represents $\text{NIL}$ but has all the attributes of other objects in the list. References to $\text{NIL}$ are replaced by references to $L.nil$. This change turns a regular doubly linked list onto a **circular, doubly linked list with a sentinel**, in which the sentinel $L.nil$ lies between the head and tail. The attribute $L.nil.next$ points to the head of the list, and $L.nil.prev$ points to the tail. Similarly, both the $next$ attribute of the tail and the $prev$ attribute of the head point to $L.nil$. Since $L.nil.next$ points to the head, the attribute $L.head$ is eliminated all together, with references to it replaced by references to $L.nil.next$. An an empty list consists of just the sentinel, and both $L.nil.next$ and $L.nil.prev$ point to $L.nil$.

To delete an element from the list, just use the two-line procedure defined above. Just as `LIST_INSERT` never references object $L$, neither does the new `LIST_DELETE` procedure. You should never delete the sentinel unless you are deleting the entire list. The procedure below inserts an element $x$ into the list following object $y$. No separate procedure for prepending is necessary: to insert at the head of the list, let $y$ be $L.nil$; and do insert at the tail, let $y$ be $L.nil.prev$

```powershell
LIST_INSERT(x, y)
    x.next = y.next
    x.prev = y
    y.next.prev = x
    y.next = x
```

Searching a circular, doubly linked list with a sentinel has the same asymptotic running time as without a sentinel, but it is possible to decrease the constant factor. The test on line 2 of `LIST_SEARCH` makes two comparisons. One to check whether the search has run off the end of the list and, if not, to check whether the key resides in the current element $x$. Suppose that you know that the key is somewhere in the list. Then you need to check whether the search runs off the end of the list, thereby eliminating one comparison in each iteration of the `while` loop.

The sentinel provides a place to put the key before starting the search. The search starts at the head $L.nil.next$ of list $L$, and it stops if it finds the key somewhere in the list. Now the search is guaranteed to find the key, either in the sentinel or before reaching it. If the key is found before, then it really is in the element where the search stops. However, if the search goes through all the elements in the list and find the key only in the sentinel, then the key is not really in the list, and the search returns $\text{NIL}$. The procedure below embodies this idea. (If your sentinel requires its $key$ attribute to be $\text{NIL}$, then you might assign $L.nil.key = \text{NIL}$ before line 5):

```powershell
LIST_SEARCH(L, k)
    L.nil.key = k    # Store the key in the sentinel to guarantee it is in the list
    x = L.nil.next   # Start at the head of the list
    while x.key != k
        x = x.next
    if x == L.nil    # Found k in the sentinel
        return NIL   # k was not really in the list
    else
        return x     # Found k in element x
```

Sentinels often simplify code, as in searching a linked list, they might speed up code by a small constant factor, but they don't typically improve the asymptotic running time. Use them judiciously. When there are many small lists, the extra storage used by sentinels can waste significant amounts of memory. Only use them when they significantly simplify the code.