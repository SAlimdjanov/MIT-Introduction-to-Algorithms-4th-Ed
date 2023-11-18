# Standard Notations and Common Functions

## Monotonicity

A function $f(n)$ is **monotonically increasing** if $m \le n$ implies $f(m) \le f(n)$. A function is **monotonically decreasing** if $m \le n$ implies $f(m) \ge f(n)$.

A function $f(n)$ is **strictly increasing** if $m < n$ implies $f(m) < f(n)$. A function is **strictly decreasing** if $m < n$ implies $f(m) > f(n)$.

## Floors and Ceilings

For any real number $x$, we denote the greatest integer less than or equal to $x$ by the floor of $x$, $\lfloor x \rfloor$ and the least integer greater than or equal to $x$ by the ceiling of $x$, $\lceil x \rceil$. The floor function is monotonically increasing, as is the ceiling function. Floors and ceilings obey the following properties:

For any integer $n$:

$$\lfloor n \rfloor = n = \lceil n \rceil$$

For all real $x$:

$$x - 1 < \lfloor x \rfloor \le x \le \lceil x \rceil < x + 1$$
$$- \lfloor x \rfloor = \lceil -x \rceil$$
$$- \lceil x \rceil = \lfloor -x \rfloor$$

For any real number $x \ge 0$ and integers $a, b > 0$:

$$\left\lceil \frac{\lceil x / a \rceil }{b} \right\rceil = \left\lceil \frac{x}{ab} \right\rceil$$

$$\left\lfloor \frac{\lfloor x / a \rfloor }{b} \right\rfloor = \left\lfloor \frac{x}{ab} \right\rfloor$$

$$\left\lceil \frac{a}{b} \right\rceil \le \frac{a + (b - 1)}{b}$$

$$\left\lfloor \frac{a}{b} \right\rfloor \ge \frac{a - (b - 1)}{b}$$

For any integer $n$ and real number $x$:

$$\lfloor n + x \rfloor = n + \lfloor x \rfloor $$
$$\lceil n + x \rceil = n + \lceil x \rceil $$

## Modular Arithmetic

For any integer $a$ and any positive integer $n$, the value $a \text{ mod } n$ is the remainder of the quotient $a / n$:

$$ a \text{ mod } n = a - n \lfloor a / n \rfloor$$

Follows that (even when $a$ is negative):

$$ 0 \le a \text{ mod } n < n$$

If $(a \text{ mod } n) = (b \text{ mod } n)$, we write $a = b (\text{mod } n)$ if $a$ and $b$ have the same remainder when divided by $n$. $a = b (\text{mod } n)$ if and only if $n$ is a divisor of $b - a$. We write $a \ne b (\text{mod } n)$ if $a$ is not equivalent to $b$ modulo $n$.

## Polynomials

Given a nonnegative integer $d$, a **polynomial in n of degree $d$** is a function $p(n)$ of the form:

$$p(n) = \sum\limits_{i = 0}^d {a_i n^i}$$

Where the constants $a_0, a_1, ..., a_d$ are the coefficients of the polynomial and $a_d \ne 0$. A polynomial is asymptotically positive if and only if $a_d > 0$. For an asymptotically positive polynomial $p(n)$ of degree $d$, we have $p(n) = \Theta(n^d)$. For any real constant $a \ge 0$, the function $n^a$ is monotonically increasing, and for any real constant $a \le 0$, the function $n^a$ is monotonically decreasing. We say that a function $f(n)$ is **polynomially bounded** if $f(n) = O(n^k)$ for some constant $k$.

## Exponentials

For all real $a > 0$, $m$, and $n$, we have:

$$
\begin{align*}
a^0 &= 1 \\
a^1 &= a \\
a^{-1} &= \frac{1}{a} \\
(a^m)^n &= a^{nm} \\
(a^m)^n &= (a^n)^m \\
a^m a^n &= a^{m + n}
\end{align*}
$$

For all $n$ and $a \ge 1$, the function $a^n$ is monotonically increasing in $n$. When convenient, we assume $0^0 = 1$. We can relate the growth of polynomials and exponentials by the following fact; For all real constants $a > 1$ and $b$:

$$\lim_{n \rightarrow \infin} {\frac{n^b}{a^n}} = 0$$

From which we can conclude that $n^b = o(a^n)$. Thus, for any exponential function with a base strictly greater than $1$ grows faster than any polynomial function. We have for all real $x$:

$$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + ... = \sum\limits_{i = 0}^{\infin}{\frac{x^i}{i!}}$$

For all real $x$, we have the inequality:

$$1 + x \le e^x$$

The equality holds when $x = 0$. When $|x| \le 1$, we have the approximation:

$$1 + x \le e^x \le 1 + x + x^2$$

When $x \rightarrow 0$, the approximation of $e^x$ by $1 + x$ is quite good:

$$e^x = 1 + x + \Theta(x^2)$$

We have for all $x$:

$$\lim_{n \rightarrow \infin} {\left(1 + \frac{x}{n}\right)^n} = e^x$$

## Logarithms

We use the following notations:

$$
\begin{align*}
\lg n &= \log_2 n \text{ (Binary Logarithm)} \\
\ln n &= \log_e n \text{ (Natural Logarithm)}\\
\lg^k n &= (\lg n)^k \text{ (Exponentiation)} \\
\lg \lg n &= \lg (\lg n) \text{ (Composition)}\\
\end{align*}
$$

For any constant $b > 1$, the function $\log_b n$ is undefined if $n \le 0$, strictly increasing if $n > 0$, positive if $n > 1$, and $0$ if $n = 1$. For all real $a, b, c > 0$, and $n$:

$$
\begin{align*}
a &= b^{\log_b a} \\
\log_c (ab) &= \log_c a + \log_c b \\
\log_b a^n &= n \log_b a \\
\log_b a &= \frac{\log_c a}{\log_c b} \\
\log_b (1 / a) &= - \log_b a \\
\log_b a &= \frac{1}{\log_a b} \\
a^{\log_b c} &= a^{\log_b a}
\end{align*}
$$

In each equation above, logarithm bases are not $1$. There is a simple series expansion for $\ln(x + 1)$ when $|x| < 1$:

$$\ln(x + 1) = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + ...$$

We also have the following inequalities for $x > -1$:

$$\frac{x}{1 + x} \le \ln(x + 1) \le x$$

Where the above inequality is only equal when $x = 0$. We say that a function $f(n)$ is **polylogarithmically bounded** if $f(n) = O(\lg^k n)$ for some constant $k$. We can relate the growth of polynomials and polylogarithms by substituting $\lg n$ for $n$ and $2^a$ for $a$ from the conclusion drawn in the previous section. For all real constants $a > 0$ and $b$, we have:

$$\lg^b n = o(n^a)$$

Thus, any positive polynomial function grows faster than any polylogarithmic function.

## Factorials

Defined for integers $n \ge 0$ as:

$$
n!=  \left\{
\begin{array}{ll}
      1, & n = 0 \\
      n \cdot (n - 1)!, & n > 0 \\
\end{array}
\right.
$$

Thus, $n! = 1 \cdot 2 \cdot 3 \cdot \cdot \cdot n$. A weak upper bound on the factorial is $n! \le n^n$, since each of the $n$ terms in the factorial product is at most $n$. **Stirling's approximation**, where $e$ is the base of the natural logarithm, gives a tight upper bound, and a lower bound as well:

$$n! = \sqrt{2 \pi n} \left( \frac{n}{e} \right)^n \left( 1 + \Theta \left( \frac{1}{n}\right) \right)$$

The approximation yields the following expressions:

$$
\begin{align*}
n! &= o(n^n) \\
n! &= \omega (2^n) \\
\lg (n!) &= \Theta(n \lg n) \\
\end{align*}
$$

The following equation holds for all $n \ge 1$:

$$n! = \sqrt{2 \pi n} \left( \frac{n}{e} \right)^n e^{\alpha_n} \space \space \text{where} \space \space \frac{1}{12 n + 1} < \alpha_n < \frac{1}{12 n}$$

## Functional Iteration

We use the notation $f^{(i)}(n)$ to denote the function $f(n)$ iteratively applied $i$ times to an initial value of $n$. Formally, let $f(n)$ be a function over real numbers. For nonnegative integers $i$, we recursively define:

$$
f^{(i)}(n) =  \left\{
\begin{array}{ll}
      n, & i = 0 \\
      f(f^{(i - 1)}(n)), & i > 0 \\
\end{array}
\right.
$$

For example, if $f(n) = 2 n$, then $f^{(i)}(n) = 2^i n$

## Iterated Logarithm Function

We use the notation $\lg^* n$ to denote the iterated logarithm, defined as follows. Suppose we have $\lg^{(i)} n$ with $f(n) = \lg n$. Because the logarithm of a nonpositive number is undefined, $\lg^{(i)} n$ is defined only if $\lg^{(i - 1)} n > 0$. Then we define the iterated logarithm as:

$$
\lg^* n = \text{min} \left\{
\begin{array}{ll}
    i \ge 0 : \lg^{(i) n} \le 1
\end{array}
\right\}
$$

The iterated logarithm grows very slowly.

## Fibonacci Numbers

We define the Fibonacci numbers $F_i$, for $i \ge 0$ as:

$$
F_i =  \left\{
\begin{array}{ll}
      0, & i = 0 \\
      1, & i = 1 \\
      F_{i - 1} + F_{i - 2}, & i \ge 2 \\
\end{array}
\right.
$$

Fibonacci numbers are related to the **golden ratio** $\phi$ and its conjugate $\hat{\phi}$, which are the two roots of the equation: $x^2 = x + 1$:

$$ \phi = \frac{1 + \sqrt 5}{2} \space \text{ and } \space \hat{\phi} = \frac{1 - \sqrt 5}{2} $$

With respect to the Fibonacci number:

$$ F_i = \frac{\phi^i - \hat{\phi^i}}{\sqrt 5}$$
