# Divide and Conquer: Recurrences

## Recall: Divide and Conquer

Recall the steps for a Divide-and-Conquer Algorithm (if the base case is not met):

1.  **Divide** the problem into one or more subproblems that are smaller instances of the same problem
2.  **Conquer** the subproblems by solving them recursively
3.  **Combine** the subproblem solutions to form a solution to the original problem

## Recurrences

A **recurrence** is an equation that describes a function in terms of its value on other, typically smaller, arguments. Recurrences go hand in hand with the divide-and-conquer method because they give us a natural way to characterize the running times of recursive algorithms mathematically. The general form of a recurrence is an equation or inequality that describes a function over the integers or reals using the function itself. It contains two or more cases, depending on the argument. If a case involves the recursive invocation of the function on different (usually smaller) inputs, it is a **recursive case**. There may be one, zero, or many functions that satisfy the statement of the recurrence. The recurrence is **well defined** if there is at least one function that satisfies it, and **ill defined** otherwise.

## Algorithmic Recurrences

A recurrence $T(n)$ is **algorithmic** if, for every sufficiently large **threshold constant** $n_0 < 0$, the following two properties hold:

1.  For all $n < n_0$, we have $T(n) = \Theta(1)$
2.  For all $n \ge n_0$, every path of recursion terminates in a defined base case within a finite number of recursive invocations

When a function is not defined for all arguments, this definition is constrained to values of $n$ for which $T(n)$ is defined.

## Conventions for Recurrences

We adopt the following convention: _Whenever a recurrence is stated without an explicit base case, we assume that the recurrence is algorithmic_

This means that one is free to select any sufficiently large threshold constant $n_0$ for the range of base cases where $T(n) = \Theta(1)$. In most algorithms, the asymptotic solutions don't depend on the choice of $n_0$, as long as $n_0$ is large enough, the recurrence is well defined. Asymptotic solutions of algorithmic divide-and-conquer recurrences don't tend to change when floors and/or ceilings are dropped.

Sometimes recurrences are inequalities and not equations. For example, $T(n) \le 2 T(n / 2) + \Theta(n)$. Because such a recurrence states only an upper bound on $T(n)$, we express its solution using $O$-notation instead. If the inequality previously mentioned was reversed, $\Omega$-notation is used in its solution.

## Divide and Conquer Recurrences

Although it is common for divide-and-conquers to divide a problem into subproblems of the same size, this isn't always the case. Sometimes it is more productive to divide into subproblems of different sizes, and then the recurrence describing the running time reflects the irregularity. Some divide-and-conquer algorithms usually create subproblems with sizes a constant fraction of the original problem size, this is also not always the case.
