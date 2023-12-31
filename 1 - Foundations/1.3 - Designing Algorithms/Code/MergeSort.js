/*
 * MergeSort.js
 *
 */

function merge(array, start, midpoint, end) {
    let lenLeft = midpoint - start + 1;
    let lenRight = end - midpoint;

    let left = new Array(lenLeft).fill(0);
    let right = new Array(lenRight).fill(0);

    for (let i = 0; i < lenLeft; i++) {
        left[i] = array[start + i];
    }

    for (let j = 0; j < lenRight; j++) {
        right[j] = array[midpoint + j + 1];
    }

    let i = 0,
        j = 0,
        k = start;

    while (i < lenLeft && j < lenRight) {
        if (left[i] <= right[j]) {
            array[k] = left[i];
            i += 1;
        } else {
            array[k] = right[j];
            j += 1;
        }
        k += 1;
    }

    while (i < lenLeft) {
        array[k] = left[i];
        i += 1;
        k += 1;
    }

    while (j < lenRight) {
        array[k] = right[j];
        j += 1;
        k += 1;
    }
}

function mergeSort(array, start, end) {
    if (start >= end) {
        return;
    }

    let midpoint = Math.floor((start + end) / 2);

    mergeSort(array, start, midpoint);
    mergeSort(array, midpoint + 1, end);

    merge(array, start, midpoint, end);
}

module.exports = mergeSort;
