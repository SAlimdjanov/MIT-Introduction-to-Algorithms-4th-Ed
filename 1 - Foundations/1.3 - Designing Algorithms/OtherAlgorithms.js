/*
 * OtherAlgorithms.js
 *
 * JavaScript implementation of Other Algorithms
 *
 */

function bubbleSort(array) {
    const n = array.length;
    for (var i = 0; i < n; i++) {
        for (var j = n - 1; j > -1; j--) {
            if (array[j] < array[j - 1]) {
                let temp = array[j];
                array[j] = array[j - 1];
                array[j - 1] = temp;
            }
        }
    }
}

function hornerRule(array, x) {
    const n = array.length;
    var result = 0;
    for (var i = n - 1; i > -1; i--) {
        result = array[i] + x * result;
    }
    return result;
}

var array = [2, 4, 6, 7, 1, 2, 3, 5, 8, 10, 9];
const polynomialCoeff = [1, 2, 3, 0, 4]; // 1 + 2x + 3x^2 + 4x^4

bubbleSort(array);
console.log(array);

p = hornerRule(polynomialCoeff, 5);
console.log(p);
