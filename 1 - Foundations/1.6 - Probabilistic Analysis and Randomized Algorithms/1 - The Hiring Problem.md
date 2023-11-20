# The Hiring Problem

The `HIRE_ASSISTANT` procedure expresses a strategy for hiring. The candidates for the office assistant job are numbered $1$ through $n$ and are interviewed in that order. The procedure assumes that after interviewing candidate $i$, you can determine whether candidate $i$ is the best candidate you have seen so far. It starts by creating a dummy candidate numbered $0$, who is less qualified than each of the other candidates:

```python
HIRE_ASSISTANT(n)
    best = 0  # Dummy candidate
    for i = 1 to n
    interview candidate i
    if candidate i is better than candidate 'best'
        best = i
        hire candidate i
```

Interviewing has a low cost, say $c_i$, whereas hiring is expensive, costing $c_h$. Let $m$ be the number of people hired, the total cost associated with this algorithm is $O(c_i n + c_h m)$.

This scenario serves as a model for a common computational paradigm. Algorithms often need to find the maximum or minimum value in a sequence by examining each element of the sequence and maintaining a current "winner."

## Worst-Case Analysis

In the worst case, you hire every candidate that you interview. This situation occurs of the candidates come in strictly increasing orders of quality, in which case you can hire $n$ times, for a total hiring cost of $O(c_h n)$.

## Probabilistic Analysis

**Probabilistic analysis** is the use of probability in the analysis of problems. Most commonly, we use probabilistic analysis to analyze the running time of an algorithm. Sometimes we use it to analyze other quantities, such as the hiring cost in the procedure above.

In order to perform a probabilistic analysis, we must use knowledge of (or assume) the distribution of the inputs. Then we analyze the algorithm, computing an average-case running time, where we take the average (or expected) value, over the distribution of possible inputs. When reporting such a running time, we refer to it as the **average-case running time**. In problems that you cannot characterize a reasonable input distribution, you cannot use probabilistic analysis.

For the hiring problem, we can assume that the applicants come in a random order. What does that mean for the problem? We assume that you can compare any two candidates and decide which one is better qualified, which is to say there is a total order on the candidates. Thus, you rank each candidate with a unique number from $1$ through $n$, using $rank(i)$ to denote the rank of applicant $i$, and adopt the convention that a higher rank corresponds to a better qualified applicant. The ordered list $\left< rank(1), ..., rank(n)\right>$ is a permutation of the list $\left<1, ..., n \right>$. Saying that the applicants come in a random order is equivalent to saying that this list of ranks is equally likely to be any one of the $n!$ permutations of the numbers $1$ through $n$. Alternatively, we say that the ranks form a **uniform random permutation**, that is, eauch of the possible $n!$ permutations appears with equal probability.

##  Randomized Algorithms

In many cases, you know little about the input distribution. Even if something is known, you might not be able to model this knowledge computationally. Probability and randomness often serve as tools for algorithm design and analysis, by making part of the algorithm behave randomly.

In the hiring problem, you have no idea about whether the candidates are actually presented in a random order. Thus, to develop a randomized algorithm for the hiring problem, you need greater control over the order in which you'll interview the candidates. We will therefore change the model slightly. The employment agency will send a list of the $n$ candidates in advance. On each day, you randomly choose a candidate to interview.

More generally, we call an algorithm **randomized** if its behavior is determined not only by its input but also by values produced by a random number generator `RANDOM(a, b)`. For example, `RANDOM(0, 1)` returns $0$ or $1$ with a probability of $1 / 2$ for both.

When analyzing the running time of a randomized algorithm, we take the expectation of the running time over the distribution of values returned by the random number generator. We distinguish these algorithms from those in which the input is random by referring to the running time of a randomized angorithm as an **expected running time**. In general, the average case running time is discussed with these algorithms.