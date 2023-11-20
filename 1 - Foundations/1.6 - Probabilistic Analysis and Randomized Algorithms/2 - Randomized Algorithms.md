# Randomized Algorithms

For the hiring problem, the only change needed in the code is to permute the list of candidates:

```python
RANDOMIZED_HIRE_ASSISTANT(n)
    # randomly permute the list of candidates
    HIRE_ASSISTANT(n)
```

**Lemma:** _The expected hiring cost of the_ `RANDOMIZED_HIRE_ASSISTANT` _procedure is_ $O(c_h \ln n)$.

## Randomly Permuting Arrays

This method of generating a random permutation permutes the array **in place**: at most a constant number of elements of the input array are ever stored outside the array. The procedure below permutes an array $A[1: n]$ in place in $\Theta(n)$ time:

```python
RANDOMLY_PERMUTE(A, n)
    for i = 1 to n
        swap A[i] with A[RANDOM(i, n)]
```

We use a loop invariant to show that this procedure produces a uniform random permutation. A **$k$-permutation** on a set of $n$ elements is a sequence containing $k$ of the $n$ elements, with no repititions. There are $n! / (n - k)!$ such possible permutations.

## The Online Hiring Problem

Suppose now you do not wish to interview all the candidates to find the best one. You also want to avoid hiring and firing as you find better applicants. Instead, you are willing to settle for a candidate who is close to the best, in exchange for hiring only once.

We can model this problem in the following way. After meeting an applicant, you are able to give each one a score. Let $score(i)$ denote the score you give to the $i$-th applicant, and assume no two applicants receive the same score. After you have seen $j$ applicants, you know which of the $j$ has the highest score, but you do not know whether any of the remaining $j - n$ applicants will receive a better score. You decide to adopt the strategy of selecting a positive integer $k < n$, interviewing and rejecting the first $k$ candidates, and hiring the applicant thereafter who has the higher score than all precedding applications. It turns out that the best-qualified applicant was among the first $k$ interviewed, then you hire the $n$-th applicant, the last one interviewed. This strategy is formalized in the procedure below:

```python
ONLINE_HIRING_PROBLEM(k, n)
    best score = -inf
    for i = 1 to k
        if score(i) > best score
            best score = score(i)
    for k = i + 1 to n
        if score(i) > best score
            return i
    return n
```