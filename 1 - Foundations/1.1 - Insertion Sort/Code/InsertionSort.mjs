/*
 * InsertionSort.mjs
 *
 * JavaScript implementation of Insertion Sort and related problems.
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

const main = () => {
    const inputList = [5, 2, 4, 6, 1, 3];
    const binA = [1, 0, 1, 0];
    const binB = [1, 1, 1, 1];

    console.log(insertionSort(inputList, inputList.length));
    console.log(insertionSortReversed(inputList, inputList.length));
    console.log(binaryArrayAddition(binA, binB, binA.length));
};

// main();

export default insertionSort;
