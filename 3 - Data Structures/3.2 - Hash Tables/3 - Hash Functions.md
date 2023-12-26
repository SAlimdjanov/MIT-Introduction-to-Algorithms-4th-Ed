# Hash Functions

For hashing to work well, it needs a good hash function. Along with being efficiently computable, what properties does a good hash function have?

### What Makes a Good Hash Function?

A good hash function approximately satisfies the assumption of independent uniform hashing: each key is equally likely to hash to any of the $m$ slots, independently of where any other keys have hashed to. Unfortunately, there is no way to check if the probability distribution of the input keys is equal. Additionally, the keys might not be drawn independently. If the distribution is known, for example, it is known that the keys are random real numbers $k$ independently and uniformly distributed in the range $0 \le k < 1$, then the hash function $h(k) = \lfloor km \rfloor$ satisfies the condition of independent uniform hashing.

### Keys are Integers, Vectors, or Strings

In practice, a hash function is designed to handle keys that are one of the following two types:

-   A short nonnegative integer that fits in a $w$-bit machine word. Typical values for $w$ would be $32$ or $64$
-   A short vector of nonnegative integers, each of bounded size. For example, each element might be an $8$-bit byte, in which case the vector is often called a byte string. The vector might be of variable length.

For now, assume that keys are short nonnegative integers. Handling vector keys is more complicated.

## Static Hashing

Static hashing uses a single, fixed hash function. The only randomization available is through the (usually known) distribution of input keys. Although static hashing is no longer recommended, the multiplication method also provides a good foundation for "nonstatic" hashing - better known as random hashing - where the hash function is chosen at random from a suitable family of a hash functions.

### Division Method

The **division method** for creating hash function maps a key $k$ into one of $m$ slots by taking the remainder of $k$ divided by $m$. The hash function is:

$$h(k) = k \text{ mod } m$$

For example, if the hash table has size $m = 12$ and the key is $k = 100$, then $h(k) = 4$. Since it requires only a single division operation, hashing by division is quite fast. The division method may work well when $m$ is a prime not too close an exact power of $2$. There is no guarantee that this method provides good average-case performance, however, it may complicate applications since it constrains the size of the hash tables to be prime.

### Multiplication Method

The general **multiplication method** for creating hash functions operates in two steps. First, multiply the key $k$ by a constant $A$ in the range $0 < A < 1$ and extract the fractional part of $kA$. Then, multiply this value by $m$ and take the floor of the result. The hash function is:

$$h(k) = \lfloor m (kA \text{ mod } 1)\rfloor$$

where $kA \text{ mod } 1$ means the fractional part of $kA$, that is, $kA - \lfloor kA \rfloor$. The general multiplication method has the advantage that the value of $m$ is not critical and you can choose it independently of how you choose the multiplicative constant $A$.

### Multiply-Shift Method

In practice, the multiplication method is best in the special case where the number $m$ of hash-table slots is an exact power of $2$, so that $m = 2^l$ for some integer $l$, where $l \le w$ and $w$ is the number of bits in a machine word. If you choose a fixed $w$-bit positive integer $a = A 2^w$, where $0 < A < 1$ as in the multiplication method so that $a$ is in the range $0 < a < 2^w$, you can implement the function on most computers as follows. Assume that a key $k$ fits into a single $w$-bit word.

First multiply $k$ by the $w$-bit integer $a$. The result is a $2w$-bit value $r_1 2^w + r_0$, where $r_1$ is the high-order $w$-but word of the product and $r_0$ is the low-order $w$-bit word of the product. The desired $l$-bit hash value consisted of the $l$ most significant bit of $r_0$. Since $r_1$ is ignored, the hash function can be implemented on a computer that produces only a $w$-bit product given two $w$-bit inputs, that is, where the multiplication operation computes modulo $2^w$. In other words, the hash function $h = h_a$ is:

$$h_a(k) = (ka \text{ mod } 2^w) >>> (w - l)$$

Where $a$ is a fixed nonzero $w$-bit value. Since the product $ka$ of two $w$-bit words occupies $2w$ bits, taking this product modulo $2^w$ zeroes out the high-order $w$ bits ($r_1$), leaving only the low-order $w$ bits ($r_0$). The $>>>$ operator performs a logical right shift by $w - l$ bits, shifting zeros into the vacated positions on the left, so that the $l$ most significant bits of $r_0$ move into the $l$ rightmost positions. The resulting value equals the $l$ most significant bits of $r_0$. The hash function $h_a$ can be implemented with three machine instructions: multiplication, subtraction, and logical right shift. Even though this method is fast, it doesn't provide any guarantee of good average-case performance.

## Random Hashing

Suppose that a malicious adversary choses the keys to be hashed by some fixed hash function. The adversary can choose $n$ keys that all hash to the same slot, yielding an average retrieval time of $\Theta(n)$. Any static hash function is vulnerable to such terrible worst-case behavior. The only effective way to improve the situation is the choose the hash function randomly in a way that is independent of the keys that are actually going to be stored. This approach is called **random hashing**, can yield provably good performance on average when collisions are handled by chaining, no matter which keys the adversary chooses.

To use random hashing, at the beginning of program execution you select the hash function at random from a suitable family of functions. As in the case of quicksort, randomization guarantees that no single input always evokes the worst-case behavior. Because you randomly select the hash function, the algorithm can behave differently on each execution, even for the same set of keys to be hashed, guaranteeing a good average-case performance.

Let $H$ be a finite family of hash functions that map a given universe $U$ of keys into the range $\set{0, 1, ..., m - 1}$. Such a family is said to be universal if for each pair of distinct keys $k_1, k_2 \in U$, the number of hash functions $h \in H$ for which $h(k_1) = h(k_2)$ is at most $|H| / m$. In other words, with a hash function randomly chosen from $H$, the chance of a collision between distinct keys $k_1$ and $k_2$ is no more than the chance $1 / m$ of a collision if $h(k_1)$ and $h(k_2)$ were randomly and independently chose from the set $\set{0, 1, ..., m - 1}$.

Independent uniform hashing is the same as picking a hash function uniformly at random from a family of $m^n$ hash functions, each member of that family mapping the $n$ keys to the $m$ hash values in a different way. Every independent uniform random family of hash function is universal, but the converse need not to be true: consider the case $U = \set{0, 1, ..., m - 1}$ and the only hash function in the family is the identity function. The probability that two distinct keys collide is zero, even though each key hashes to a fixed value.

_**Corollary:** Using universal hashing and collision resolution by chaining in an initially empty table with_ $m$ _slots, it takes_ $\Theta(s)$ _expected time to handle any sequence of_ $s \text{ INSERT, SEARCH}$ _and_ $\text{DELETE}$ _operations containing_ $n = O(m) \text{ INSERT}$ _operations_.

## Achievable Properties of Random Hashing

There is a rich literature on the properties a $H$ of hash functions can have, and how they relate to the efficiency of hashing. Let $H$ be a family of hash functions, each with domain $U$ and range $\set{0, 1, ..., m - 1}$, and let $h$ be any hash function that is uniformly picked at random from $H$. The probabilities mentioned are probabilities over the picks of $h$.

-   The family $H$ is **uniform** if for any key $k$ in $U$ and any slot $q$ in the range $\set{0, 1, ..., m - 1}$, the probability that $h(k) = q$ is $1 / m$
-   The family $H$ is **universal** if for any distinct keys $k_1$ and $k_2$ in $U$, the probability that $h(k_1) = h(k_2)$ is at most $1 / m$
-   The family of hash functions is $\epsilon$-**universal** if for any distinct keys $k_1$ and $k_2$ in $U$, the probability that $h(k_1) = h(k_2)$ is at most $\epsilon$. Therefore, a universal family of hash functions is also $1 / m$-universal.
-   The family $H$ is **d-independent** if for any distinct keys $k_1, k_2, ..., k_d$ in $U$ and any slots $q_1, q_2, ..., q_d$, not necessarily distinct, in $\set{0, 1, ..., m - 1}$ the probability that $h(k_i) = q_i$ for $i = 1, 2, ..., d$ is $1 / m^d$

Universal hash-function families are of particular interest, as they are the simplest type supporting provably efficient hash-table operations for any input data set. Many other interesting and desirable properties, such as those noted above, are also possible and allow for efficient specialized hash-table operations.

## Designing a Universal Family of Hash Functions

Here, two ways to design a universal (or $\epsilon$-universal) family of hash functions: one based on number theory and another based on a randomized variant of the multiply-shift method.

### A Universal Family of Hash Functions Based on Number Theory

We can design a universal family of hash functions using number theory. Begin by choosing a prime number $p$ large enough so that every possible key $k$ lies in the range $0$ to $p - 1$, inclusive. We assume that $p$ has a reasonable length. Let $ℤ_p$ denote the set $\set{0, 1, ..., p - 1}$, and let $ℤ_p^*$ denote the set $\set{1, 2, ..., p - 1}$. Because the size of the universe of keys is greater than the number of slits in the hash table (otherwise, just use direct addressing), we have $p > m$.

Given any $a \in ℤ_p^*$ and any $b \in ℤ_p$, define the hash function $h_{ab}$ as a linear transformation followed by reductions modulo $p$ and then module $m$:

$$
h_{ab} (k) = \left[(ak + b) \text{ mod } p\right] \text{ mod } m
$$

Given $p$ and $m$, the family of all such hash functions is:

$$
H_{pm} = \set{h_{ab}: a \in ℤ_p^* \text{ and } b \in ℤ_p}
$$

Each hash function $h_{ab}$ maps $ℤ_p$ to $ℤ_m$. The family of hash functions has the nice property that the size $m$ of the output range (which is the size of the hash table) is arbitrary - it need not be prime. Since you can choose from among $p - 1$ values for $a$ and $p$ values for $b$, the family $H_{pm}$ contains $p(p - 1)$ hash functions.

_**Theorem:** The family_ $H_{pm}$ _of hash functions defined by the previous two equations._

### A $2 / m$-Universal Hash Functions Based on the Multiply-Shift Method

In practice, this method is recommended. It is exceptionally efficient and is provably $2 / m$ universal:

$$h_a(k) = (ka \text{ mod } 2^w) >>> (w - l)$$

Define $H$ to be family of multiply-shift hash functions with odd constants $a$:

$$
H = \set{h_a: a \text{ is odd, } 1 \le a < m}
$$

Therefore, the probability that two any distinct keys collide is at most $2 / m$. In many practical situations, the speed of computing the hash function more than compensates for the higher upper bound on the probability that two distinct keys collide when compared with a universal hash function.

## Hashing Long Inputs such as Vectors or Strings

Sometimes hash function inputs are so long that they cannot be easily encoded modulo a reasonably sized prime number $p$ or encoded within a single word of, for example, $64$ bits. As an example, consider the class of vectors of $8$-bit bytes (which is how strings in many programming language). A vector might have an arbitrary nonnegative length, in which case the length of the input to the hash function may vary from input to input.

### Number Theoretic Approaches

One way to design good hash functions for variable-length inputs is to extend the ideas used in section "A Universal Family of Hash Functions based on Number Theory". One approach is as follows.

Let $U$ be the set of $d$-tuples of values drawn from $ℤ_p$, and let $Q = ℤ_p$, where $p$ is prime. Define the hash function $h_b : U \rightarrow Q$ for $b \in ℤ_p$ on an input $d$-tuple $\left< a_0, a_1, ..., a_{d - 1}\right>$ from $U$ as:

$$
h_b (\left< a_0, a_1, ..., a_{d - 1}\right>) = \left( \sum \limits_{a_j}^{d - 1} a_j b^j \right) \text{ mod } p
$$

Furthermore, let $H = \set(h_b: b \in ℤ_p)$. $H$ is $\epsilon$-universal for $\epsilon = (d - 1) / p$.

### Cryptographic Hashing

**Cryptographic hash functions** are complex pseudorandom functions, designed for applications requiring properties beyond those needed here, but are robust, widely implemented, and usable as hash functions for hash tables.

A cryptographic hash function takes as input an arbitrary byte string and returns a fixed-length output. For example, the NIST standard deterministic cryptographic hash function SHA-256 [346] produces a $256$-bit ($32$-byte) output for any input. Some chip manufacturers include instructions in their CPU architectures to provide fast implementations of some cryptographic functions. Of particular interest are instructions that are effectively implement rounds of the Advanced Encryption Standard (AES), the "AES-NI" instructions. These instructions execute in a few tens of nanoseconds, which is generally fast enough for use with hash tables. A message authentication code such as CBC-MAC based on the AES and the use of the AES-NI instructions could be a useful and efficient hash function.

Cryptographic hash functions are useful because they provide a way of implementing an approximate version of a random oracle. Theoretically, a random oracle is not possible to achieve. From a practicle point of view, constructions of hash function families based on cryptographic hash functions are sensible substitutes for random oracles. For example:

$$h(k) = \text{SHA-256}(k) \text{ mod } m$$

To define a family of such hash functions one may prepend a "salt" string $a$ to the input before hashing it, as in:

$$h(k) = \text{SHA-256}(a || k) \text{ mod } m$$

where $a || k$ denotes the string formed by concatenating the strings $a$ and $k$. The literature on message authentication codes (MACs) provides additional approaches. Cryptographic approaches to hash-function design are becoming more practical as computers arrange their memories in heirarchies of differing capacities and speeds.

