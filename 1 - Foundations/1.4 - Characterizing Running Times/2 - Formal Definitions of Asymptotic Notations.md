# Formal Definitions of Asymptotic Notations

## $O$-Notation

For a given function $g(n)$, we denote by $O(g(n))$ the set of functions:

$$
O(g(n)) =
\set{
    f(n) : \text{there exist positive constants } c \text{ and } n_0 \text{ such that } 0 \le f(n) \le c g(n) \text{ for all } n \ge n_0
}
$$

A function $f(n)$ belongs to the set $O(g(n))$ if there exists a positive constant $c$ such that $f(n) \le c g(n)$ for sufficiently large $n$. This definition requires all functions in the set to be **asymptotically nonnegative:** $f(n)$ must be nonnegative whenever $n$ is sufficiently large. (An **asymptotically positive** function is one that is positive for all sufficently large $n$) Consequently, the function $g(n)$ itself must be asymptotically nonnegative, or else the set $O(g(n))$ is empty. We therefore assume that every function used within $O$-notation is asymptotically nonnegative. This assumption holds for other notations discussed here.

#### Example

Show that $4 n^2 + 100 n + 500 = O(n^2)$

We need to find constants $c$ and $n_0$ such that $4 n^2 + 100 n + 500 \le c n^2$ for all $n \ge n_0$. Dividing both sides by $n^2$ gives:

$$ 4 + \frac{100}{n} + \frac{500}{n^2} \le c$$

This inequality is satisfied for many choices of $c$ and $n_0$. We can also use the formal definition of $O$-notation to show that the function $n^3 - 100 n^2$ does not belong to the set $O(n^2)$, even though the coefficient of $n^2$ is a large negative number. If this function was in the set, there would be no positive constants $c$ and $n_0$ such that $n^3 - 100 n^2 \le c n^2$.

## $\Omega$-Notation

For a given function $g(n)$, we denote by $\Omega(g(n))$ the set of functions:

$$
\Omega(g(n)) =
\set {
    f(n) : \text{there exist positive constants } c \text{ and } n_0 \text{ such that } 0 \le c g(n) \le f(n) \text{ for all } n \ge n_0
}
$$

#### Example

Show that $4 n^2 + 100 n + 500 = \Omega(n^2)$

We need to find constants $c$ and $n_0$ such that $4 n^2 + 100 n + 500 \ge c n^2$ for all $n \ge n_0$. Dividing both sides by $n^2$ gives $ 4 + 100 / n + 500 / n^2 \ge c$. This inequality holds when $n_0$ is any positive integer and $c = 4$. What if we subtracted the lower-order terms from the $4 n^2$ term instead of adding them? What if we had a small coefficient for the $n^2$ term? The function would still be $\Omega(n^2)$. For example, let's show that $n^2 / 100 - 100 n - 500 = \Omega(n^2)$. Dividing by $n^2$ gives $1 / 100 - 100/ n - 500 / n^2 \ge c$. We can choose any value for $n_0 \ge 10,005$ and find a positive value for $c$.

## $\Theta$-Notation

For a given function $g(n)$, we denote by $\Theta(g(n))$ the set of functions:

$$
\Theta(g(n)) =
\set{
    f(n) : \text{there exist positive constants } c_1, c_2 \text{ and } n_0 \text{ such that } 0 \le c_1 g(n) \le f(n) \le c_2 g(n) \text{ for all } n \ge n_0
}
$$

The previous definitions lead to the following theorem:

**Theorem:** _For any two functions_ $f(n)$ _and_ $g(n)$, _we have_ $f(n) = \Theta(g(n))$ _if and only if_ $f(n) = O(g(n))$ _and_ $f(n) = \Omega(g(n))$.

Therefore, proving that a function is satisfies the definitions of $O$ and $\Omega$ notations, you can conclude that the function is also $\Theta$.

## $o$-Notation

The asymptotic upper bound provided by $O$-notation may or may not be asymptotically tight. We use $o$-notation to denote an upper bound that is not asymptotically tight. We formally define $o(g(n))$ as the set:

$$
o(g(n)) =
\set{
    f(n) : \text{for any positive constant } c > 0, \text{ there exists a constant } n_0 > 0 \text{ such that } 0 \le f(n) < c g(n) \text{ for all } n \ge n_0
}
$$

For example, $2 n = o(n^2)$, but $2 n^2 \ne o(n^2)$. The definitions of $O$-notation and $o$-notation are similar. The main difference is that in $f(n) = O(g(n))$, the bound $0 \le f(n) \le c g(n)$ holds for some constants $c > 0$, but in $f(n) = o(g(n))$, the bound $0 \le f(n) < c g(n)$ holds for all constants $c > 0$. In $o$-notation, the function $f(n)$ becomes insignificant relative to $g(n)$ as $n$ gets large:

$$\lim_{n \rightarrow \infty} {\frac{f(n)}{g(n)}} = 0$$

This definition restricts the anonymous functions to be asymptotically nonnegative.

## $\omega$-Notation

By analogy, $\omega$-notation is to $\Omega$-notation as $o$-notation is to $O$-notation. We use $\omega$-notation to denote a lower bound that is not asymptotically tight. One way to define it is:

$$f(n) \in \omega(g(n)) \text{ if and only if } g(n) \in o(f(n))$$

The formal definition is that $\omega(g(n))$ is in the set:

$$
\omega(g(n)) =
\set{
    f(n) : \text{for any positive constant } c > 0, \text{ there exists a constant } n_0 > 0 \text{ such that } 0 \le c g(n) < f(n) \text{ for all } n \ge n_0
}
$$

Where the definition of $o$-notation says that $f(n) < c g(n)$, this says the opposite: that $c g(n) < f(n)$. For examples of $\omega$-notation, we have $n^2 / 2 = \omega(n)$, but $n^2 / 2 \ne \omega(n^2)$. The relation $f(n) = \omega(g(n))$ implies that:

$$\lim_{n \rightarrow \infty} {\frac{f(n)}{g(n)}} = \infty$$

If the limit exists. That is $f(n)$ becomes arbitrarily large relative to $g(n)$ as $n$ gets large.
