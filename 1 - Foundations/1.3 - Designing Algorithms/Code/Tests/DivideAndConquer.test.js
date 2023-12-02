/**
 * DivideAndConquer.test.js
 *
 */

const bubbleSort = require("../BubbleSort");
const hornersRule = require("../HornersRule");
const mergeSort = require("../MergeSort");

test("bubbleSort sorts correctly", () => {
    const array = [2, 4, 6, 7, 1, 2, 3, 5, 8, 10, 9];
    bubbleSort(array);

    const sorted = [...array];
    sorted.sort((a, b) => a - b);

    expect(array).toStrictEqual(sorted);
});

test("hornersRule evaluates the polynomial correctly", () => {
    const polynomialCoeff = [1, 2, 3, 0, 4];
    const answer = 2586;

    let p = hornersRule(polynomialCoeff, (x = 5));

    expect(p).toStrictEqual(answer);
});

test("mergeSort sorts correctly", () => {
    const array = [2, 4, 6, 7, 1, 2, 3, 5];

    const sorted = [...array];
    sorted.sort((a, b) => a - b);

    mergeSort(array, 0, 7);

    expect(array).toStrictEqual(sorted);
});
