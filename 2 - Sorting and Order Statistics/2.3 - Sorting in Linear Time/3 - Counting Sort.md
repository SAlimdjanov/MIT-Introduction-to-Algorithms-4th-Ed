# Counting Sort

**Counting sort** assumes that each of the $n$ input elements is an integer in the range $0$ to $k$, for some integer $k$. It runs in $\Theta(n + k)$ time, so that when $k = O(n)$, counting sort runs in $\Theta(n)$ time.

Counting sort first determines, for each input element $x$, the number of elements less than or equal to $x$. It then uses this information to place element $x$ directly into its position in the output array. For example, if $17$ elements are less than or equal to $x$, then $x$ belongs in output position $17$. Slight modification of this scheme is necessary to handle the situation in which several elements have the same value, since we do not want them all to end up in the same position.

The `COUNTING_SORT` procedure takes an array $A[1: n]$, the size of the array $n$, and the limit $k$ on the nonnegative integer values in $A$ as inputs. It returns its sorted output in the array $B[1: n]$ and uses an array $C[0: k]$ for temporary working storage.

```shell
COUNTING_SORT(A, n, k)
let B[1: n] and C[0: k] be new arrays
for i = 0 to k
    C[i] = 0
for j = 1 to n
    C[A[j]] = C[A[j]] + 1
# C[i] now contains the number of elements equal to i
for i = 1 to k
    C[i] = C[i] + C[i - 1]
# C[i] now contains the number of elements less than or equal to i
# Copy A to B, starting from the end of A
for j = n down to 1
    B[C[A[j]]] = A[j]
    C[A[j]] = C[A[j]] - 1  # Handle duplicate values
return B
```

After the first `for` loop initializes the array `C` to all zeros, for second `for` loop makes a pass over `A` to inspect each input element. Each time it finds an input element whose value is `i`, it increments `C[i]`. After this loop, `C[i]` holds the number of elements equal to $i$ for each integer $0, 1, ..., k$. The third `for` loop determines for each $i = 0, 1, ..., k$ how many input elements are less than or equal to $i$ by keeping a running sum of the array `C`.

The last `for` loop makes another pass over `A` in reverse, to place each element `A[j]` into its correct sorted position in the output array `B`. If all $n$ elements are correct, then when the last loop is first entered, for each `A[j]`, the value `C[A[j]]` is the correct final position of `A[j]` in the output array, since there are `C[A[j]]` elements less than or equal to `A[j]`. Because the elements might not be distince, the loop decrements `C[A[j]]` each time it places a value `A[j]` into `B`. Decrementing `C[A[j]]` causes the previous element in `A` with a value equal to `A[j]`, if one exists, to go to the position immediately before `A[j]` in the output array `B`.

## Analysis

The first loop takes $\Theta(k)$ time, the second takes $\Theta(n)$ time, the third loop takes $\Theta(k)$ time, and the last one takes $\Theta(n)$ time. Thus, the overall time takes $\Theta(n + k)$ time. In practice, we usually use counting sort when we have $k = O(n)$, in which case the running time is $\Theta(n)$.

Counting sort can beat the lower bound of $\Omega(n \lg n)$ previously discussed because it is not a comparison sort. In fact, no comparisions actually occur anywhere in the procedure. Instead, counting sort uses the actual values of the elements to index into the array. This lower bound does not apply.

An important property of counting sort is that it is **stable**: elements with the same value appear in the output array in the same order as they do in the input array. It breaks ties between two elements by the rule that whichever element appears first in the input array appears first in the output array. Normally, the property of stability is important only when satellite data are carried around with the element being sorted. Counting's stability is important for another reason, it is often used as a subrouting in radix sort (next section).