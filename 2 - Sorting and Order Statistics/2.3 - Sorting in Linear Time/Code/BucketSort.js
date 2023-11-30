/**
 * BucketSort.js
 *
 */

function bucketSort(array, n) {
    let auxArray = Array.from({ length: n }, () => []);

    for (let i = 0; i < n; i++) {
        let index = Math.floor(n * array[i]);
        auxArray[index].push(array[i]);
    }

    for (let i = 0; i < n; i++) {
        auxArray[i].sort();
    }

    let sortedArray = [];

    for (let i = 0; i < n; i++) {
        sortedArray = sortedArray.concat(auxArray[i]);
    }

    return sortedArray;
}

module.exports = bucketSort;
