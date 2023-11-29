/**
 * BucketSort.mjs
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

const main = () => {
    let array = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21];
    let result = bucketSort(array, array.length);
    console.log(result);
};

main();

export default bucketSort;
