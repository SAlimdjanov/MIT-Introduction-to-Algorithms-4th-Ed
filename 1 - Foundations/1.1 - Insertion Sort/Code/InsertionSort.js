/*
 * InsertionSort.js
 *
 */

function insertionSort(sequence, n) {
    for (let i = 0; i < n; i++) {
        let key = sequence[i];

        let j = i - 1;
        while (j >= 0 && sequence[j] > key) {
            sequence[j + 1] = sequence[j];
            j -= 1;
        }

        sequence[j + 1] = key;
    }
    return sequence;
}

function insertionSortReversed(sequence, n) {
    for (let i = 0; i < n; i++) {
        let key = sequence[i];

        let j = i - 1;
        while (j >= 0 && sequence[j] < key) {
            sequence[j + 1] = sequence[j];
            j -= 1;
        }

        sequence[j + 1] = key;
    }
    return sequence;
}

function binaryArrayAddition(binA, binB, n) {
    let binC = new Array(n + 1).fill(0);
    let carryBit = 0;

    for (let i = n - 1; i > -1; i--) {
        let total = binA[i] + binB[i] + carryBit;
        binC[i + 1] = total % 2;
        carryBit = Math.floor(total / 2);
    }
    binC[0] = carryBit;

    return binC;
}

module.exports = { insertionSort, insertionSortReversed, binaryArrayAddition };
