/**
 * CountingSort.js
 *
 */

function countingSort(array, n, k) {
    let sortedOutput = Array(n).fill(0);

    let memoLength = k + 1;
    let memo = Array(memoLength).fill(0);

    for (let i = 0; i < n; i++) {
        memo[array[i]] = memo[array[i]] + 1;
    }

    for (let j = 1; j <= k; j++) {
        memo[j] = memo[j] + memo[j - 1];
    }

    for (let x = n - 1; x > -1; x--) {
        sortedOutput[memo[array[x]] - 1] = array[x];
        memo[array[x]] = memo[array[x]] - 1;
    }

    return sortedOutput;
}

module.exports = countingSort;
