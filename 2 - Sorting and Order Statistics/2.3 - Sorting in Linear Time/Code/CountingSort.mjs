/**
 * CountingSort.mjs
 *
 */

function countingSort(array, n, k) {
    let sortedOutput = new Array(n).fill(0);

    let memoLength = k + 1;
    let memo = new Array(memoLength).fill(0);

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

const main = () => {
    let duplicateArray = [6, 0, 2, 0, 1, 3, 4, 6, 3, 1, 2];
    let result1 = countingSort(
        duplicateArray,
        duplicateArray.length,
        Math.max(...duplicateArray)
    );
    console.log(result1);

    let array = [0, 2, 7, 3, 4, 6, 5, 1, 8];
    let result2 = countingSort(array, array.length, Math.max(...array));
    console.log(result2);
};

// main();

export default countingSort;
